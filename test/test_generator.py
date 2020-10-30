import pytest

from haystack import Document
import numpy as np

DOCS_WITH_EMBEDDINGS = [
    Document(
        text="""The capital of Germany is the city state of Berlin.""",
        embedding=np.array([2.22920075e-01, 1.07770450e-02, 3.35382462e-01, -7.27265477e-02,
                           -1.98119566e-01, -5.64537346e-02, 6.09261453e-01, 2.87229061e-01,
                           -7.73971230e-02, -2.23876238e-01, -5.47461927e-01, -1.08676875e+00,
                           2.95721531e-01, 7.53905892e-01, -3.36153835e-01, 1.94666490e-01,
                           2.92297024e-02, 6.56022906e-01, 2.67616689e-01, -3.81376356e-01,
                           -2.98582464e-01, -1.89207539e-01, 6.07246757e-01, 1.67709842e-01,
                           2.75577039e-01, -9.33986664e-01, 4.31648612e-01, -1.00929722e-01,
                           -4.82133955e-01, 7.30958655e-02, -4.85000134e-01, -1.17192902e-01,
                           -2.78178096e-01, 6.61195964e-02, 4.15457308e-01, 3.25128995e-02,
                           2.66546309e-01, 1.30013347e-01, 3.52349013e-01, -6.64731681e-01,
                           -6.83372736e-01, -3.16153020e-01, 3.67267191e-01, -4.05127078e-01,
                           -8.20419341e-02, -1.00207639e+00, -2.10523933e-01, 9.38237131e-01,
                           -2.96095699e-01, -1.82708800e-01, -9.05334055e-01, 2.68770158e-01,
                           3.29131901e-01, 9.00070250e-01, 4.34159547e-01, -5.65743327e-01,
                           -7.94787586e-01, -9.83037204e-02, -1.01550505e-01, 1.17718965e-01,
                           2.48768821e-01, 2.64568210e-01, -1.21708572e-01, 3.54779810e-01,
                           7.25113750e-01, 4.65293467e-01, -4.09185141e-02, -8.67474079e-03,
                           -2.21501254e-02, -6.34054065e-01, -9.91622388e-01, -2.93476105e-01,
                           -3.77548009e-01, -3.20685089e-01, 7.97941908e-02, -4.51179177e-01,
                           1.61721796e-01, 2.01941788e-01, 2.18551666e-01, 8.89380276e-02,
                           9.31400955e-02, -1.68867663e-01, 1.93741471e-01, 9.80174169e-03,
                           3.96567971e-01, 3.25188875e-01, -3.59817073e-02, -3.05083066e-01,
                           -2.91377038e-01, -2.59871781e-01, -2.33116597e-02, 8.39208305e-01,
                           1.92560270e-01, 1.10900663e-01, -6.46018386e-02, -7.44270265e-01,
                           1.63968995e-01, 1.13590971e-01, 2.35207364e-01, 1.82242617e-01,
                           -1.76687598e-01, 1.26516908e-01, 3.98482740e-01, 2.40804136e-01,
                           4.77896258e-02, -6.28400743e-01, -4.66124773e-01, 3.31229940e-02,
                           -2.50761136e-02, 4.35739040e-01, -2.45411038e-01, -2.20042571e-01,
                           8.92485529e-02, -4.65541370e-02, -1.38036475e-01, 5.56459785e-01,
                           5.61165631e-01, -9.59392071e-01, -2.86836233e-02, 2.67911255e-01,
                           4.45386730e-02, 8.50977540e-01, -6.11386299e-02, -1.98372751e-01,
                           4.68791090e-02, -5.06277978e-01, 1.34303793e-01, 7.62167692e-01,
                           -2.64607519e-01, 4.18876261e-02, 2.89180636e-01, 5.62154353e-01,
                           2.11251423e-01, 3.10281783e-01, 7.21961856e-02, -5.72963893e-01,
                           3.83405089e-01, 1.92931354e-01, -4.10556868e-02, 6.54039383e-02,
                           -7.69101679e-01, -3.99726629e-01, 4.27413732e-04, -8.61558840e-02,
                           6.74372464e-02, -6.33262277e-01, 1.29509404e-01, -7.98301876e-01,
                           -1.86452359e-01, -3.74487117e-02, 6.27469346e-02, 5.53238690e-01,
                           -1.18287519e-01, 2.22255215e-01, -3.88892442e-01, -5.07142544e-02,
                           1.17656231e+00, 1.06320940e-01, 4.87917721e-01, 1.30945101e-01,
                           5.19872069e-01, -5.09424150e-01, 7.24166155e-01, 2.54679173e-02,
                           4.71467018e-01, 2.11418241e-01, 7.24739254e-01, 8.81170094e-01,
                           5.08289784e-03, -2.56663375e-02, -7.88815022e-01, -3.99944574e-01,
                           4.35373336e-01, -1.85048744e-01, -3.40764970e-03, -3.34966034e-02,
                           -5.41758597e-01, 1.26321182e-01, 2.60807693e-01, 6.73399121e-03,
                           -2.97145188e-01, 8.47041607e-01, -9.33591202e-02, 5.28455973e-01,
                           -3.99243206e-01, 1.12693250e-01, -1.43983305e-01, 1.67462572e-01,
                           -5.15321195e-02, 4.32413101e-01, 4.54831392e-01, -4.17369545e-01,
                           2.24987328e-01, -7.20562488e-02, 1.14134535e-01, 4.92308468e-01,
                           -8.98665905e-01, 5.71145713e-01, -4.19293523e-01, 3.95240694e-01,
                           1.14924744e-01, -6.05691969e-01, 5.72251439e-01, -2.09341362e-01,
                           -2.33997151e-01, 1.25237420e-01, 1.88679054e-01, -1.65349171e-01,
                           1.09286271e-01, 3.67127098e-02, -8.38237703e-02, -7.06058443e-01,
                           2.02231467e-01, -2.55237550e-01, 1.09513953e-01, -1.31659687e-01,
                           -6.15252674e-01, -3.03829938e-01, 1.37894958e-01, -4.24786448e-01,
                           4.53196496e-01, -1.98051147e-02, -4.47584987e-01, 2.15226576e-01,
                           1.43030539e-01, 1.77718982e-01, -7.88647681e-02, 5.66962123e-01,
                           -4.94479597e-01, -2.12739050e-01, -6.91644847e-03, 3.48478556e-02,
                           -1.28705889e-01, -3.83449569e-02, 5.88934198e-02, -6.58130586e-01,
                           -5.36214471e-01, 2.55122989e-01, 8.75554740e-01, -4.75414962e-01,
                           9.52955902e-01, 1.35785684e-01, 1.23120442e-01, 5.05717754e-01,
                           1.48803160e-01, 4.04200435e-01, 2.76372820e-01, -2.47299239e-01,
                           -8.07143569e-01, 4.83604342e-01, -1.85374618e-01, -1.95024580e-01,
                           -1.25921816e-01, 7.70030096e-02, 1.42136604e-01, -3.08087885e-01,
                           1.59089297e-01, 3.25954586e-01, 1.59884766e-01, 6.17780030e-01,
                           2.01809742e-02, -3.50671440e-01, -6.72550499e-01, 4.13817167e-03,
                           -2.71146059e-01, 7.78259337e-02, -2.49091178e-01, -3.05263430e-01,
                           2.25365594e-01, 3.72759551e-01, 3.85581732e-01, -1.09396994e-01,
                           -3.47314715e-01, -1.12919524e-01, 1.29915655e-01, 8.06079060e-03,
                           3.92060950e-02, 1.97335854e-02, -6.53263927e-01, -1.24800075e-02,
                           -1.32480651e-01, 7.22689390e-01, -2.42579862e-01, -1.25441504e+00,
                           -1.32172257e-02, -1.10918665e+00, 8.78458321e-01, -3.46063733e-01,
                           -3.95923197e-01, 7.50630498e-01, -6.05472811e-02, 3.24168801e-03,
                           -1.87530309e-01, 1.40227765e-01, -2.82838583e-01, 1.33317798e-01,
                           1.89625695e-01, -8.86574462e-02, 2.12340951e-01, -2.99456716e-01,
                           -1.22753668e+00, 3.14115554e-01, -6.14668578e-02, 5.75566962e-02,
                           4.74531233e-01, -4.22935635e-01, -4.82785627e-02, 1.42783090e-01,
                           -5.56570292e+00, -3.73210102e-01, -3.54320705e-01, -4.24514055e-01,
                           -2.42527917e-01, 6.06708586e-01, 1.82795480e-01, 4.26353738e-02,
                           -3.05563331e-01, -5.30404389e-01, 8.72441947e-01, 1.09079361e-01,
                           2.24435870e-02, 6.74964964e-01, 2.53065675e-01, 3.88592303e-01,
                           1.19709507e-01, -3.20065737e-01, -3.31855297e-01, -2.44884327e-01,
                           -3.52100194e-01, -2.81845808e-01, 8.55575204e-01, 1.62181407e-01,
                           7.85247564e-01, -2.96381339e-02, -2.88497955e-01, 6.53568059e-02,
                           -7.08795369e-01, -8.04900110e-01, 4.42439765e-02, -4.29058880e-01,
                           3.26467693e-01, -1.53244287e-01, 3.99080157e-01, 4.89609912e-02,
                           4.12760764e-01, 3.94182920e-01, 1.94052160e-01, -4.93394583e-01,
                           -2.29200646e-02, 4.95266408e-01, -6.72604218e-02, 1.91921741e-02,
                           5.96645474e-01, -2.27546245e-01, -1.71159700e-01, -5.57102934e-02,
                           -8.21766138e-01, 5.46978891e-01, 7.12940097e-02, 2.39723727e-01,
                           3.99156392e-01, -4.60546672e-01, -3.68922651e-01, 4.64805663e-01,
                           9.51609537e-02, 4.60486412e-01, -4.56739873e-01, 1.10822640e-01,
                           -2.06528842e-01, 1.95380542e-02, -1.97392479e-01, -1.14359230e-01,
                           -2.01808512e-02, -1.26127511e-01, -7.95332611e-01, 6.66711032e-01,
                           2.22024679e-01, 7.37181231e-02, -2.25423813e-01, -8.22625279e-01,
                           2.40563720e-01, -6.11137688e-01, -6.11412823e-01, -1.45952356e+00,
                           -1.37649477e-04, -5.29529095e-01, 1.47666246e-01, 3.54295582e-01,
                           -6.83852911e-01, 1.97373703e-01, -1.56224251e-01, -1.39315836e-02,
                           1.52347326e-01, -1.78363323e-01, -2.45118767e-01, 4.62190807e-02,
                           6.59810960e-01, -5.49332023e-01, -3.59251350e-01, -8.36586714e-01,
                           4.37820464e-01, -7.46994615e-01, -6.13222957e-01, 5.13272882e-01,
                           -8.53794441e-02, -5.95119596e-01, 6.63125142e-02, -2.91639060e-01,
                           3.56542349e-01, -2.10935414e-01, -6.86178625e-01, -4.68558609e-01,
                           2.96867311e-01, 1.22527696e-01, 3.36856037e-01, 6.65121257e-01,
                           8.23574543e-01, -4.33361620e-01, -4.60013747e-01, 9.83969793e-02,
                           -2.06140336e-02, -9.26007748e-01, 4.21539873e-01, -1.04092360e+00,
                           -8.31346154e-01, 7.40615308e-01, 2.03596890e-01, -3.54458541e-01,
                           -1.00714087e-01, 6.06378078e-01, -1.25727594e-01, -7.54246935e-02,
                           -4.75891769e-01, -8.33747163e-03, -7.37221539e-01, 8.11691880e-02,
                           -4.76147123e-02, 1.16448052e-01, 6.71404898e-02, 8.09732974e-02,
                           4.06575024e-01, -6.49466589e-02, 6.71445608e-01, 1.64475188e-01,
                           2.04286948e-01, -3.85309786e-01, -1.56549439e-01, -7.14797437e-01,
                           2.02202156e-01, 5.64372897e-01, 3.26015085e-01, 1.32548913e-01,
                           7.73424655e-02, -3.40584129e-01, -1.97809264e-02, 2.23556265e-01,
                           -4.01336968e-01, -6.39470071e-02, 8.09292793e-01, 6.28170550e-01,
                           -6.66837394e-03, -1.85917675e-01, -8.26690435e-01, 2.90101707e-01,
                           3.71746987e-01, 3.63382846e-01, 3.30177546e-01, -1.59507245e-01,
                           4.05810446e-01, -6.38260722e-01, -4.45926607e-01, 3.86468828e-01,
                           5.87992489e-01, -1.67837348e-02, -8.56421649e-01, -1.46168426e-01,
                           1.47883758e-01, -3.02581072e-01, 3.04086179e-01, -3.63289267e-01,
                           -1.37931064e-01, 2.16311902e-01, -2.87937909e-01, 2.17867494e-01,
                           1.85905039e-01, 2.63448834e-01, 3.99643362e-01, 7.09417015e-02,
                           -7.54964426e-02, -5.97936213e-01, -4.81102228e-01, 8.86633337e-01,
                           -2.07774624e-01, 4.67518479e-01, 2.69507207e-02, 3.04756582e-01,
                           1.97698742e-01, 2.01897427e-01, 7.08150089e-01, -1.89206481e-01,
                           -2.48630807e-01, 1.31412342e-01, -3.77624273e-01, -8.65468025e-01,
                           2.81697720e-01, 2.68136449e-02, -3.59579533e-01, -1.67907849e-01,
                           3.39563519e-01, 5.14352739e-01, -5.05458474e-01, 1.13890879e-01,
                           5.56517914e-02, -2.44290620e-01, 5.04581273e-01, 6.74505532e-02,
                           1.21912472e-01, 3.03465098e-01, -1.17531466e+00, -2.73063779e-03,
                           -2.87389159e-01, 5.57524502e-01, -4.76101369e-01, -2.24274755e-01,
                           6.08418345e-01, -8.36228848e-01, -2.73688063e-02, 1.36113301e-01,
                           4.85431179e-02, 3.30218256e-01, 2.45848745e-02, -2.14380369e-01,
                           -1.55451417e-01, 4.74268287e-01, -5.26949689e-02, -3.60365629e-01,
                           1.46594465e-01, -7.30531573e-01, 4.51633155e-01, -5.78917377e-02,
                           -1.14988096e-01, -5.43769002e-02, -5.84075786e-02, -1.25919655e-01,
                           3.54636490e-01, 1.66502092e-02, -2.82013208e-01, 1.53901696e-01,
                           7.34325886e-01, 6.29021525e-01, 1.65552661e-01, -2.53647298e-01,
                           2.58286983e-01, -2.23352492e-01, 1.37091652e-01, -7.11111128e-02,
                           -7.29316473e-01, 3.14306825e-01, -1.94846138e-01, -1.88290656e-01,
                           -5.51873147e-01, -5.86067080e-01, 7.76780128e-01, -3.32203567e-01,
                           1.26009226e-01, 6.82506114e-02, 2.42465541e-01, -4.79260236e-01,
                           -2.64422894e-01, -1.46414991e-02, -1.63076729e-01, 4.91135448e-01,
                           -7.55948648e-02, -4.34874535e-01, -4.70796406e-01, 2.31533051e-01,
                           6.86599091e-02, -4.67249811e-01, -3.49846303e-01, -1.56457052e-01,
                           2.26900756e-01, -3.05055201e-01, 5.14786020e-02, 7.42341399e-01,
                           3.08751971e-01, 3.73778671e-01, -3.72706920e-01, 4.08769280e-01,
                           -4.39344704e-01, 9.28550214e-03, 2.11898744e-01, -8.82063210e-01,
                           2.79842377e-01, -9.61523890e-01, -1.06504209e-01, 4.37725782e-01,
                           -6.85699284e-01, -7.09701329e-02, 2.03018457e-01, -7.74664462e-01,
                           -3.58985692e-01, 2.29817599e-01, -1.63717717e-02, 3.96644741e-01,
                           3.03747296e-01, 7.59450972e-01, 3.05326551e-01, 1.13241032e-01,
                           -3.04896057e-01, 7.16535866e-01, 5.99493623e-01, -3.41223150e-01,
                           8.01769421e-02, 2.74060369e-01, -1.89308211e-01, -7.03582019e-02,
                           6.31491482e-01, -2.66766787e-01, -3.60058993e-02, -4.59694006e-02,
                           4.13341448e-02, 6.20938718e-01, -4.05673683e-01, 3.14955115e-01,
                           8.51010144e-01, -1.57450408e-01, 1.32778615e-01, 3.33602667e-01,
                           -1.68273598e-01, -8.25519502e-01, 3.41632813e-01, 2.60136947e-02,
                           1.49609357e-01, 3.42133522e-01, 3.76624107e-01, -1.45224094e-01,
                           -6.06691055e-02, 1.32190138e-01, 1.17674023e-01, 7.03091204e-01,
                           -5.53888232e-02, 1.80667877e-01, -9.27466691e-01, -2.98746169e-01,
                           1.82669535e-01, 5.05023301e-01, -4.15828198e-01, 4.03008044e-01,
                           2.74655282e-01, 5.33584476e-01, -2.66726196e-01, 3.71005863e-01,
                           6.66988790e-01, -2.88121644e-02, -3.36296678e-01, -4.08127680e-02,
                           2.42406055e-01, -3.95779252e-01, 6.24649882e-01, -2.11524870e-02,
                           -9.01915729e-02, 6.27994537e-04, 2.01389760e-01, -2.37837404e-01,
                           2.33498871e-01, 2.53635406e-01, -1.48279428e-01, -1.29509941e-01,
                           1.57033205e-01, -3.17683131e-01, 9.30176303e-03, 2.08731264e-01,
                           -2.70904571e-01, 1.72909975e-01, -2.84282975e-02, -1.26348920e-02,
                           -5.57500660e-01, -4.00371701e-01, 4.37779486e-01, 2.39513844e-01,
                           -9.83366221e-02, -4.74843085e-01, 7.46401250e-02, 2.65029907e-01,
                           -2.55706310e-01, -4.04609382e-01, 6.11083746e-01, 2.09431499e-01,
                           -4.90902215e-01, -3.79809409e-01, -4.07738805e-01, -8.39593947e-01,
                           -4.45040494e-01, 1.32427901e-01, -2.89512202e-02, -4.05294597e-01,
                           1.10134587e-01, 2.92823054e-02, -7.39422813e-03, -3.82603586e-01,
                           2.00942218e-01, -1.56378612e-01, -6.31098151e-02, -8.38923037e-01,
                           2.18381509e-01, 4.24017191e-01, -1.11921988e-02, -2.06086934e-02,
                           8.83747578e-01, 2.98153669e-01, -1.01949327e-01, 3.51015419e-01,
                           1.73736498e-01, 4.60796833e-01, -1.50092870e-01, -4.06093806e-01,
                           -5.45160949e-01, 8.19314718e-02, 5.16103089e-01, -8.94221127e-01,
                           -2.19182819e-01, 3.07301104e-01, -2.76391618e-02, -1.36747360e-01,
                           3.67395580e-01, -3.47063392e-01, -2.81705800e-02, 1.09726787e-02,
                           2.90009379e-02, -2.60963470e-01, 4.64340061e-01, 7.83061028e-01,
                           4.33903933e-01, 2.94982612e-01, 8.19467902e-01, 6.35938764e-01,
                           -4.21458691e-01, 3.45274419e-01, -7.68046618e-01, -5.41747689e-01,
                           -8.85769799e-02, 1.31434202e-01, -5.25221646e-01, 4.55112815e-01,
                           6.91722155e-01, 6.68683171e-01, -5.47426462e-01, -7.70461857e-01,
                           -1.66969776e-01, 4.41468775e-01, 5.66215217e-01, 3.57928425e-02,
                           2.17262149e-01, -9.86621380e-02, -4.86463368e-01, 2.94643529e-02,
                           -8.25751781e-01, 3.90646994e-01, 3.40370983e-01, 3.16112041e-01,
                           9.32825267e-01, -1.61067862e-02, 2.67292827e-01, -3.85537408e-02,
                           3.50360483e-01, -4.22007769e-01, 8.67691994e-01, 1.73017085e-01],
                           dtype=np.float32)
    ),
    Document(
        text="""Berlin is the capital and largest city of Germany by both area and population.""",
        embedding=np.array([-3.50273997e-02, -2.48432189e-01, 6.22839212e-01, -2.02022746e-01,
                           -3.85405064e-01, 2.25520879e-01, 3.62649381e-01, 5.04554689e-01,
                           -4.23478037e-01, -3.49022627e-01, -3.92042458e-01, -1.29845297e+00,
                           2.67841876e-01, 8.42141330e-01, -1.04595557e-01, 3.08678299e-01,
                           2.04692081e-01, 4.04445529e-01, 1.46137536e-01, 4.34402674e-02,
                           -2.07350522e-01, -1.23709336e-01, 6.03435040e-01, 2.23109469e-01,
                           4.06399101e-01, -8.63346577e-01, 6.71044067e-02, -1.64094806e-01,
                           -2.01718658e-01, 2.26681113e-01, -4.99083489e-01, 3.95566672e-02,
                           -2.56573886e-01, 1.36661112e-01, 4.94901866e-01, -3.79223824e-01,
                           4.39944714e-02, 7.74090067e-02, 1.65991753e-01, -6.05902374e-01,
                           -6.71969056e-01, -3.25198919e-01, 4.57322180e-01, -5.73203489e-02,
                           -1.81668729e-01, -9.46653485e-01, -3.48476291e-01, 7.92435110e-01,
                           -5.79158902e-01, -5.66574708e-02, -8.12117040e-01, 2.75338925e-02,
                           1.85874030e-01, 8.35340858e-01, 4.10750836e-01, -3.47608507e-01,
                           -8.52427721e-01, 2.69759744e-02, -3.20787787e-01, -2.51891077e-01,
                           4.47721303e-01, 3.11386466e-01, -1.98152617e-01, 4.73785162e-01,
                           9.63908017e-01, 1.64340034e-01, 3.54560353e-02, -6.74128532e-03,
                           -8.14039856e-02, -7.24786401e-01, -7.03148484e-01, -2.28851557e-01,
                           -4.46531236e-01, -1.46620423e-01, -2.65437990e-01, -5.92449844e-01,
                           1.21022910e-02, 2.23394483e-03, 1.67981237e-01, -1.21683285e-01,
                           -1.35042474e-01, -3.92371416e-01, 2.45243281e-01, -1.92256197e-01,
                           5.04460752e-01, 2.30800226e-01, -3.78899246e-01, -2.25738496e-01,
                           -4.10815418e-01, -2.89627165e-01, -2.01466121e-02, 6.42084002e-01,
                           3.61558765e-01, 7.81632885e-02, -8.87344405e-02, -5.39395750e-01,
                           1.73859358e-01, 2.29152858e-01, 1.93723273e-02, -1.40379012e-01,
                           -2.77711898e-01, 1.50807753e-01, 4.77448404e-01, 5.50886393e-02,
                           -8.28208998e-02, -6.45287335e-01, -2.45338172e-01, 2.00820148e-01,
                           5.36505699e-01, 1.91126034e-01, -2.88397133e-01, -3.70828032e-01,
                           -7.51306936e-02, -4.33721125e-01, -2.39529923e-01, 2.26737723e-01,
                           3.62281471e-01, -6.49121046e-01, 7.34182149e-02, -1.84938148e-01,
                           -1.40600190e-01, 6.90262318e-01, -4.20865417e-03, 3.37241292e-02,
                           -1.04037970e-01, -5.12658119e-01, 2.85518885e-01, 6.14049435e-01,
                           -3.64280075e-01, -1.79104939e-01, -3.40193689e-01, 6.93493247e-01,
                           1.68136895e-01, 8.19072276e-02, -1.26587659e-01, -2.71052718e-01,
                           -1.73928216e-03, 5.96372664e-01, -1.99492872e-01, -1.85374454e-01,
                           -8.67393851e-01, -3.30342293e-01, -1.45058334e-01, -5.84702380e-03,
                           -1.16527915e-01, -5.52076221e-01, -1.82155043e-01, -9.68754411e-01,
                           1.34406865e-01, -2.16481060e-01, 1.59609109e-01, 7.34762907e-01,
                           -5.40787280e-01, 1.33426115e-01, -1.09678365e-01, -2.30006188e-01,
                           1.11722279e+00, 1.23066463e-01, 5.51491082e-01, 1.47878438e-01,
                           2.54464090e-01, -5.22197366e-01, 6.91881776e-01, 9.90326330e-03,
                           2.30611145e-01, -2.40993947e-02, 8.55854809e-01, 4.04415131e-01,
                           -4.35511768e-02, 2.06272732e-02, -4.83772397e-01, -3.05012941e-01,
                           4.56852138e-01, 1.49446487e-01, -3.67835537e-02, -7.69569874e-02,
                           -6.35296702e-02, 7.86715373e-02, 3.23589087e-01, -3.12235892e-01,
                           -3.00187111e-01, 6.28162324e-01, -1.43585145e-01, 7.48719096e-01,
                           1.29490951e-02, 4.96434420e-02, -2.50086904e-01, 4.04200941e-01,
                           -1.52548060e-01, 3.55123967e-01, 5.69406033e-01, -7.01724470e-01,
                           -4.43677038e-01, -3.60161997e-02, 2.70253092e-01, 2.54021317e-01,
                           -3.79845738e-01, 4.18389171e-01, -3.44766617e-01, 5.34608603e-01,
                           -3.11189979e-01, -5.41499853e-01, 3.03177029e-01, -1.43043652e-01,
                           -3.13276738e-01, 1.96103245e-01, 1.35801420e-01, -2.77429074e-02,
                           2.61924118e-01, 3.11452188e-02, 3.58356237e-02, -8.88519526e-01,
                           -4.75191772e-02, -3.92460853e-01, -8.64207298e-02, -3.05925369e-01,
                           -7.02316165e-01, -1.89588279e-01, 2.78257459e-01, -1.03573985e-01,
                           7.07532704e-01, 1.37647629e-01, -1.70264706e-01, 3.27573344e-02,
                           3.35145622e-01, 2.08075792e-02, -8.76764581e-02, 3.28958869e-01,
                           -2.38072902e-01, -3.96241456e-01, -1.07984692e-01, 1.34444326e-01,
                           -2.46238917e-01, 2.79079139e-01, -1.55260623e-01, -4.74754244e-01,
                           -2.84023583e-01, 1.02182478e-01, 1.05142117e+00, -4.61189121e-01,
                           8.53893757e-01, 1.00932568e-01, 2.80390769e-01, 6.44754589e-01,
                           4.87237096e-01, 3.82993698e-01, 1.41536862e-01, -3.36806178e-01,
                           -5.53201795e-01, 2.69606560e-01, -2.34568954e-01, -2.23571286e-02,
                           -7.33271688e-02, 4.06048372e-02, 5.10511518e-01, -2.35112339e-01,
                           3.62917244e-01, 1.57821834e-01, 4.87915903e-01, 4.96996820e-01,
                           -1.96621269e-01, -2.43224114e-01, -5.20324349e-01, 5.90502322e-02,
                           -2.56272733e-01, 3.61729294e-01, -3.32738519e-01, -5.96960723e-01,
                           2.99745977e-01, 4.65166926e-01, 3.28167796e-01, -1.17259681e-01,
                           -5.01662433e-01, -1.48999184e-01, 2.17762917e-01, -4.10884678e-01,
                           1.44081831e-01, 7.76892304e-02, -4.42914069e-01, 1.29206687e-01,
                           1.71367854e-01, 6.29935980e-01, -2.19932780e-01, -1.30284238e+00,
                           1.45756677e-01, -9.61726546e-01, 6.56495571e-01, -1.52887583e-01,
                           -2.01431572e-01, 2.95827806e-01, -2.80632555e-01, 4.25828323e-02,
                           -2.11607650e-01, -6.34967312e-02, -1.49535969e-01, 1.87844545e-01,
                           2.66154408e-01, 7.77923465e-02, 2.01846510e-01, -4.23298031e-01,
                           -1.10681295e+00, 2.42170855e-01, -6.48393482e-03, -1.13451183e-01,
                           3.46645772e-01, -5.15025079e-01, -1.29404336e-01, 3.50346863e-01,
                           -5.70772457e+00, -8.72777998e-02, -1.83941588e-01, 5.33758998e-02,
                           -2.60958552e-01, 2.95171022e-01, -8.71118158e-03, 1.90805584e-01,
                           -3.13076824e-01, -4.78946745e-01, 5.23603499e-01, 1.21371880e-01,
                           -2.50287764e-02, 7.15912938e-01, 2.29437172e-01, 2.97248602e-01,
                           2.51952589e-01, -1.86277822e-01, 9.31650400e-02, -1.53992958e-02,
                           -4.04607445e-01, -2.78155923e-01, 3.67175877e-01, 3.75201046e-01,
                           4.96505558e-01, 3.66121769e-01, -1.59621641e-01, 1.76051900e-01,
                           -8.60311389e-01, -6.75116122e-01, -1.56537183e-02, -4.97247845e-01,
                           3.06776136e-01, -4.22662735e-01, 6.39765680e-01, 2.48774216e-02,
                           2.31036097e-01, 3.25571090e-01, 9.33806449e-02, -6.65107429e-01,
                           3.17120165e-01, 4.41605687e-01, -1.78470194e-01, -2.38168150e-01,
                           7.48334885e-01, -5.21835506e-01, -3.73043060e-01, 3.62553686e-01,
                           -4.96466815e-01, 2.34892637e-01, 3.01374078e-01, 3.05527598e-01,
                           1.48040339e-01, -2.32049793e-01, -4.06453580e-01, 2.26377442e-01,
                           4.25807416e-01, 4.14450318e-01, -1.77013934e-01, 5.26809469e-02,
                           -2.83185631e-01, -1.47750434e-02, -9.70338732e-02, -4.51183803e-02,
                           5.33358902e-02, -9.44599956e-02, -2.00490251e-01, 3.36551577e-01,
                           1.70389459e-01, 6.69810623e-02, -3.73803884e-01, -3.69580567e-01,
                           2.31907159e-01, -5.82696736e-01, -6.36856616e-01, -8.39038551e-01,
                           -4.10703987e-01, -2.61468112e-01, 2.63036303e-02, 1.72604293e-01,
                           -1.00000954e+00, -1.09753408e-01, -3.69728804e-01, 7.57561699e-02,
                           2.22493976e-01, -2.52135634e-01, -4.21582580e-01, 4.54726070e-02,
                           5.95288694e-01, -1.79186583e-01, 9.71945152e-02, -7.58243561e-01,
                           6.97836161e-01, -5.38700461e-01, -2.39157140e-01, 2.57476777e-01,
                           -1.71200082e-01, -1.90746903e-01, 3.61735761e-01, 6.05483800e-02,
                           6.03016734e-01, -3.64552736e-01, -7.73001552e-01, -4.50461119e-01,
                           3.19612086e-01, 3.50916743e-01, 1.87987700e-01, 1.03144979e+00,
                           9.68851626e-01, -3.40994745e-01, -1.22335069e-01, 1.49947748e-01,
                           -1.03934139e-01, -8.34116578e-01, 6.82787180e-01, -7.01456428e-01,
                           -8.52156222e-01, 9.83630240e-01, 3.32455635e-01, -1.71249673e-01,
                           -3.09638940e-02, 6.74620807e-01, 6.88535199e-02, 1.20285749e-02,
                           -1.89996332e-01, -2.75208242e-02, -6.31824434e-01, 1.28967464e-01,
                           -3.11984301e-01, -5.88281713e-02, 1.64214373e-01, -2.94747557e-02,
                           5.38486123e-01, -1.07168958e-01, 2.51502037e-01, 2.42167205e-01,
                           3.11857104e-01, -5.06378293e-01, -1.26543716e-01, -5.85934401e-01,
                           4.25757676e-01, 7.08761454e-01, 3.90809447e-01, 2.80379802e-01,
                           -1.50237560e-01, 2.49918178e-03, -1.25070959e-01, 2.48671040e-01,
                           -2.42208377e-01, -2.54361063e-01, 6.48561537e-01, 2.21887559e-01,
                           -2.15696931e-01, 1.80307105e-01, -5.25993466e-01, 2.46874169e-01,
                           5.23397386e-01, 5.82857549e-01, 4.52213019e-01, 6.09597191e-02,
                           3.06350380e-01, -9.12604570e-01, -6.82491004e-01, -7.84439147e-02,
                           4.71254766e-01, -3.44983667e-01, -7.07369804e-01, -1.63650617e-01,
                           3.54335994e-01, -1.51956707e-01, 4.20144707e-01, -2.70185262e-01,
                           -2.19435751e-01, 1.45269379e-01, -2.86464304e-01, 2.22090811e-01,
                           -1.77325144e-01, 1.67901158e-01, 2.73082137e-01, 2.36154377e-01,
                           2.24694774e-01, -4.98087257e-01, -4.11527336e-01, 1.09001088e+00,
                           2.04774439e-01, 6.21963859e-01, -9.19686481e-02, 2.32351631e-01,
                           -1.68183297e-01, -9.68001932e-02, 5.58549523e-01, -2.39460319e-01,
                           -3.05309594e-01, 2.14133635e-01, -9.41303298e-02, -8.82585645e-01,
                           3.83934170e-01, 2.19155788e-01, -5.49660802e-01, 1.05475634e-02,
                           -6.32535443e-02, 5.38853288e-01, -6.00962579e-01, 1.27381921e-01,
                           6.89040273e-02, -2.42806375e-01, 6.02003813e-01, 2.98819840e-01,
                           2.75932997e-03, 5.27704470e-02, -1.20524478e+00, -1.19761616e-01,
                           -2.65623242e-01, 6.10629499e-01, -8.19721639e-01, -1.34642273e-02,
                           3.11588407e-01, -8.70028734e-01, -2.76728660e-01, -1.44883553e-02,
                           1.05519965e-02, 4.65373188e-01, -8.50991160e-03, -4.79901612e-01,
                           -5.53666353e-02, 6.45023704e-01, 4.40883525e-02, -3.37444067e-01,
                           1.66669071e-01, -7.71508217e-01, 4.64793175e-01, 1.12663239e-01,
                           7.72295445e-02, 2.11972415e-01, 1.04857258e-01, -2.91724950e-01,
                           3.10113102e-01, -5.58248647e-02, -2.20166266e-01, 2.14233980e-01,
                           7.40465403e-01, 3.50917518e-01, -2.04494998e-01, 3.72638553e-03,
                           2.92335540e-01, 2.86426067e-01, 2.92725444e-01, -1.24314696e-01,
                           -7.32817292e-01, -1.03724509e-01, -6.12943433e-04, -4.29165125e-01,
                           -6.33485794e-01, -4.30804014e-01, 8.27492356e-01, -4.06285793e-01,
                           3.14204842e-01, 2.00469457e-02, 4.55530435e-02, -2.90983647e-01,
                           -2.27689341e-01, -6.81395978e-02, -1.44458458e-01, 6.21065676e-01,
                           -3.66319835e-01, -3.82178009e-01, -6.32210135e-01, 1.07237205e-01,
                           -2.69225568e-01, -4.39629734e-01, -1.83134109e-01, 5.49998134e-02,
                           4.72239286e-01, -3.50412190e-01, -6.82684332e-02, 7.34665513e-01,
                           2.02386290e-01, 1.13228574e-01, -8.60403031e-02, 2.10516557e-01,
                           -3.78268421e-01, 7.76122957e-02, 1.87401593e-01, -7.81153500e-01,
                           -4.67521511e-02, -5.43340206e-01, -2.12380067e-01, 4.36673701e-01,
                           -5.81688881e-01, 5.90436339e-01, 2.56112739e-02, -8.63464177e-01,
                           -2.72117466e-01, 8.26949924e-02, -2.95551158e-02, 2.69366592e-01,
                           1.99876040e-01, 7.31362820e-01, 2.92425871e-01, 4.52556126e-02,
                           -7.45288193e-01, 6.59792423e-01, 1.32268772e-01, -7.25544393e-01,
                           1.63429856e-01, 2.86987305e-01, 2.65547365e-01, -7.67112374e-02,
                           3.05402249e-01, -3.07283700e-02, 2.72607058e-01, 1.11119784e-02,
                           5.46655431e-02, 5.27894378e-01, -5.70523500e-01, 5.23774862e-01,
                           9.90136445e-01, -2.67104745e-01, 2.66145349e-01, 8.45695660e-03,
                           -1.94764182e-01, -8.19335639e-01, 3.73185098e-01, 9.66813508e-03,
                           1.67991698e-01, 3.19511116e-01, 4.94989455e-01, -4.73073393e-01,
                           -1.90819204e-01, 1.00033917e-01, 3.54037255e-01, 3.50040078e-01,
                           -6.15488410e-01, 3.80280077e-01, -6.42622590e-01, -7.59413242e-02,
                           3.32028776e-01, 2.72891670e-01, -7.13512480e-01, 1.67983383e-01,
                           6.72589064e-01, 6.51851475e-01, -4.69424307e-01, 6.19312108e-01,
                           3.20728719e-01, 1.92631543e-01, 3.01389899e-02, 1.28930196e-01,
                           3.21145579e-02, -1.60675317e-01, 5.37545025e-01, -3.68021786e-01,
                           -3.48078310e-01, -2.95386523e-01, 1.20226748e-01, -3.62616450e-01,
                           1.78619117e-01, -1.57189220e-01, 4.32226732e-02, -6.19882271e-02,
                           -1.29041612e-01, -3.06471102e-02, 7.73153007e-02, 2.08616316e-01,
                           -8.33643898e-02, 2.84585238e-01, 2.56437182e-01, -1.31445184e-01,
                           -3.73958707e-01, -1.51229143e-01, 1.24631889e-01, 2.56145447e-01,
                           -1.46403000e-01, -5.62559128e-01, 1.44000500e-01, 7.43318856e-01,
                           -1.76492184e-01, -2.19288468e-03, 4.34121430e-01, 2.52328999e-02,
                           -1.73008680e-01, -3.12634945e-01, -3.77913564e-01, -4.67106253e-01,
                           -5.43051720e-01, -1.42914444e-01, -9.43699777e-02, -5.05417824e-01,
                           -3.18035513e-01, -9.26198438e-02, -1.14961147e-01, -3.74270320e-01,
                           2.06078768e-01, 5.94099090e-02, -1.84328973e-01, -4.85224694e-01,
                           -3.01569700e-03, 4.26463097e-01, -1.51644573e-01, 1.29547372e-01,
                           7.62950063e-01, 1.42216891e-01, -2.64579892e-01, 4.26969469e-01,
                           1.86565630e-02, 6.25447690e-01, -8.33212435e-02, -5.01296699e-01,
                           -4.33987439e-01, 2.94599593e-01, 5.06730258e-01, -4.56841111e-01,
                           -2.52863407e-01, 1.46224990e-01, -1.34221286e-01, 3.59161258e-01,
                           1.44742414e-01, -4.64949697e-01, 9.34459828e-03, -2.75842607e-01,
                           2.41558000e-01, -1.28513649e-01, 1.25265077e-01, 7.52536952e-01,
                           4.12320405e-01, 2.18520522e-01, 7.09124982e-01, 3.20003182e-01,
                           -3.68131578e-01, 3.14773470e-02, -5.25491655e-01, -1.46920130e-01,
                           -5.02151966e-01, 2.66258836e-01, -7.80072629e-01, 6.64352655e-01,
                           9.51846957e-01, 4.84095603e-01, -4.69458699e-01, -6.44100308e-01,
                           -2.09408700e-01, 1.88016608e-01, 5.53907156e-01, 2.46309891e-01,
                           3.69830072e-01, 3.00819635e-01, -5.66207170e-01, 3.10216904e-01,
                           -7.62370825e-01, 6.62293613e-01, 2.95080066e-01, 2.16252878e-01,
                           1.02028084e+00, -5.11510437e-03, 5.37559271e-01, 3.52584869e-01,
                           2.35834837e-01, -4.11791533e-01, 7.64139056e-01, 1.23637088e-01],
                           dtype=np.float32)
    )
]


@pytest.mark.slow
@pytest.mark.generator
def test_rag_token_generator(rag_generator):
    question = "What is capital of the Germany?"
    generated_docs = rag_generator.predict(question=question, documents=DOCS_WITH_EMBEDDINGS, top_k=1)
    answers = generated_docs["answers"]
    assert len(answers) == 1
    assert "berlin" in answers[0]["answer"]
