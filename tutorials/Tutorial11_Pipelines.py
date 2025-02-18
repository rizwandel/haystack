from haystack.utils import clean_wiki_text, print_answers, print_documents, fetch_archive_from_http, convert_files_to_dicts, launch_es
from pprint import pprint
from haystack import Pipeline
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import ElasticsearchRetriever, DensePassageRetriever, FARMReader, RAGenerator, JoinDocuments
from haystack.pipelines import ExtractiveQAPipeline, DocumentSearchPipeline, GenerativeQAPipeline


def tutorial11_pipelines():
    #Download and prepare data - 517 Wikipedia articles for Game of Thrones
    doc_dir = "data/article_txt_got"
    s3_url = "https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt.zip"
    fetch_archive_from_http(url=s3_url, output_dir=doc_dir)


    # convert files to dicts containing documents that can be indexed to our datastore
    got_dicts = convert_files_to_dicts(
        dir_path=doc_dir,
        clean_func=clean_wiki_text,
        split_paragraphs=True
    )

    # Initialize DocumentStore and index documents
    launch_es()
    document_store = ElasticsearchDocumentStore()
    document_store.delete_documents()
    document_store.write_documents(got_dicts)

    # Initialize Sparse retriever
    es_retriever = ElasticsearchRetriever(document_store=document_store)

    # Initialize dense retriever
    dpr_retriever = DensePassageRetriever(document_store)
    document_store.update_embeddings(dpr_retriever, update_existing_embeddings=False)

    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

    ######################
    # Prebuilt Pipelines #
    ######################

    # Extractive QA Pipeline
    ########################

    p_extractive_premade = ExtractiveQAPipeline(reader=reader, retriever=es_retriever)
    res = p_extractive_premade.run(
        query="Who is the father of Arya Stark?",
        params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}},
    )
    print_answers(res, details="minimal")

    # Document Search Pipeline
    ##########################

    p_retrieval = DocumentSearchPipeline(es_retriever)
    res = p_retrieval.run(
        query="Who is the father of Arya Stark?",
        params={"Retriever": {"top_k": 10}},

    )
    print_documents(res, max_text_len=200)

    # Generator Pipeline
    ##########################

    # We set this to True so that the document store returns document embeddings
    # with each document, this is needed by the Generator
    document_store.return_embedding = True

    # Initialize generator
    rag_generator = RAGenerator()

    # Generative QA
    p_generator = GenerativeQAPipeline(generator=rag_generator, retriever=dpr_retriever)
    res = p_generator.run(
        query="Who is the father of Arya Stark?",
        params={"Retriever": {"top_k": 10}},

    )
    print_answers(res, details="minimal")

    # We are setting this to False so that in later pipelines,
    # we get a cleaner printout
    document_store.return_embedding = False

    ##############################
    # Creating Pipeline Diagrams #
    ##############################

    p_extractive_premade.draw("pipeline_extractive_premade.png")
    p_retrieval.draw("pipeline_retrieval.png")
    p_generator.draw("pipeline_generator.png")

    ####################
    # Custom Pipelines #
    ####################

    # Extractive QA Pipeline
    ########################

    # Custom built extractive QA pipeline
    p_extractive = Pipeline()
    p_extractive.add_node(component=es_retriever, name="Retriever", inputs=["Query"])
    p_extractive.add_node(component=reader, name="Reader", inputs=["Retriever"])

    # Now we can run it
    res = p_extractive.run(
        query="Who is the father of Arya Stark?",
        params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}},
    )
    print_answers(res, details="minimal")
    p_extractive.draw("pipeline_extractive.png")

    # Ensembled Retriever Pipeline
    ##############################

    # Create ensembled pipeline
    p_ensemble = Pipeline()
    p_ensemble.add_node(component=es_retriever, name="ESRetriever", inputs=["Query"])
    p_ensemble.add_node(component=dpr_retriever, name="DPRRetriever", inputs=["Query"])
    p_ensemble.add_node(component=JoinDocuments(join_mode="concatenate"), name="JoinResults", inputs=["ESRetriever", "DPRRetriever"])
    p_ensemble.add_node(component=reader, name="Reader", inputs=["JoinResults"])
    p_ensemble.draw("pipeline_ensemble.png")

    # Run pipeline
    res = p_ensemble.run(
        query="Who is the father of Arya Stark?",
        params={"ESRetriever": {"top_k": 5}, "DPRRetriever": {"top_k": 5}},

    )
    print_answers(res, details="minimal")

    # Query Classification Pipeline
    ###############################

    # Decision Nodes help you route your data so that only certain branches of your `Pipeline` are run.
    # Though this looks very similar to the ensembled pipeline shown above,
    # the key difference is that only one of the retrievers is run for each request.
    # By contrast both retrievers are always run in the ensembled approach.

    class QueryClassifier():
        outgoing_edges = 2

        def run(self, query):
            if "?" in query:
                return {}, "output_2"
            else:
                return {}, "output_1"

    # Here we build the pipeline
    p_classifier = Pipeline()
    p_classifier.add_node(component=QueryClassifier(), name="QueryClassifier", inputs=["Query"])
    p_classifier.add_node(component=es_retriever, name="ESRetriever", inputs=["QueryClassifier.output_1"])
    p_classifier.add_node(component=dpr_retriever, name="DPRRetriever", inputs=["QueryClassifier.output_2"])
    p_classifier.add_node(component=reader, name="QAReader", inputs=["ESRetriever", "DPRRetriever"])
    p_classifier.draw("pipeline_classifier.png")

    # Run only the dense retriever on the full sentence query
    res_1 = p_classifier.run(
        query="Who is the father of Arya Stark?",
    )
    print("DPR Results" + "\n" + "="*15)
    print_answers(res_1)

    # Run only the sparse retriever on a keyword based query
    res_2 = p_classifier.run(
        query="Arya Stark father",
    )
    print("ES Results" + "\n" + "="*15)
    print_answers(res_2)


if __name__ == "__main__":
    tutorial11_pipelines()

# This Haystack script was made with love by deepset in Berlin, Germany
# Haystack: https://github.com/deepset-ai/haystack
# deepset: https://deepset.ai/
