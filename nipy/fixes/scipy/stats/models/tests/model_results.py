import numpy as np
import os
import models
from models import tools
import glm_test_resids

def generated_data():
    '''
    Returns `Y` and `X` from test_data.bin

    Returns
    -------
    Y : array
        Endogenous Data
    X : array
        Exogenous Data
    '''
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "test_data.bin")
    data = np.fromfile(filename, "<f8")
    data.shape = (126,15)
    y = data[:,0]
    x = data[:,1:]
    return y,x

### GLM MODEL RESULTS ###

class lbw(object):
    '''
    The LBW data can be found here

    http://www.stata-press.com/data/r9/rmain.html
    '''
    def __init__(self):
        # data set up for data not in datasets
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "stata_lbw_glm.csv")
        data=np.recfromcsv(filename, converters={4: lambda s: s.strip("\"")})
        data = tools.xi(data, col='race', drop=True)
        self.endog = data.low
        design = np.column_stack((data['age'], data['lwt'],
                    data['black'], data['other'], data['smoke'], data['ptl'],
                    data['ht'], data['ui']))
        self.exog = tools.add_constant(design)
        # Results for Canonical Logit Link
        self.params = (-.02710031, -.01515082, 1.26264728,
                        .86207916, .92334482, .54183656, 1.83251780,
                        .75851348, .46122388)
        self.bse = (0.036449917, 0.006925765, 0.526405169,
                0.439146744, 0.400820976, 0.346246857, 0.691623875,
                0.459373871, 1.204574885)
        self.aic_R = 219.447991133
        self.aic_Stata = 1.1611
        self.deviance = 201.447991133
        self.scale = 1
        self.llf = -100.7239955662511
        self.null_deviance = 234.671996193219
        self.bic = -742.0665
        self.df_resid = 180
        self.df_model = 8
        self.df_null = 188
        self.pearsonX2 = 182.0233425
        self.resids = glm_test_resids.lbw_resids

class cancer(object):
    '''
    The Cancer data can be found here

    http://www.stata-press.com/data/r10/rmain.html
    '''
    def __init__(self):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "stata_cancer_glm.csv")
        data = np.recfromcsv(filename)
        self.endog = data.studytime
        design = np.column_stack((data.age,data.drug))
        design = tools.xi(design, col=1, drop=True)
        design = np.delete(design, 1, axis=1) # drop first dummy
        self.exog = tools.add_constant(design)

class medpar1(object):
    '''
    The medpar1 data can be found here

    http://www.stata-press.com/data/hh2/medpar1
    '''
    def __init__(self):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "stata_medpar1_glm.csv")
        data = np.recfromcsv(filename, converters ={1: lambda s: s.strip("\"")})
        self.endog = data.los
        design = np.column_stack((data.admitype, data.codes))
        design = tools.xi(design, col=0, drop=True)
        design = np.delete(design, 1, axis=1) # drop first dummy
        self.exog = tools.add_constant(design)


class cpunish(object):
    '''
    The following are from the R script in models.datasets.cpunish
    Slightly different than published results, but should be correct
    Probably due to rounding in cleaning?
    '''
    def __init__(self):
        self.params = (2.611017e-04, 7.781801e-02, -9.493111e-02, 2.969349e-01,
                2.301183e+00, -1.872207e+01, -6.801480e+00)
        self.bse = (5.187132e-05, 7.940193e-02, 2.291926e-02, 4.375164e-01,
                4.283826e-01, 4.283961e+00, 4.146850e+00)
        self.null_deviance = 136.57281747225
        self.df_null = 16
        self.deviance = 18.59164
        self.df_resid = 10
        self.df_model = 6
        self.aic_R = 77.85466   # same as Stata
        self.aic_Stata = 4.579686
        self.bic = -9.740492
        self.llf = -31.92732831
        self.scale = 1
        self.pearsonX2 = 24.75374835
        self.resids = glm_test_resids.cpunish_resids

class scotvote(object):
    def __init__(self):
        self.params = (4.961768e-05, 2.034423e-03, -7.181429e-05, 1.118520e-04,
                -1.467515e-07, -5.186831e-04, -2.42717498e-06, -1.776527e-02)
        self.bse = (1.621577e-05, 5.320802e-04, 2.711664e-05, 4.057691e-05,
            1.236569e-07, 2.402534e-04, 7.460253e-07, 1.147922e-02)
        self.null_deviance = 0.536072
        self.df_null = 31
        self.deviance = 0.087388516417
        self.df_resid = 24
        self.df_model = 7
        self.aic_R = 182.947045954721
        self.aic_Stata = 10.72212
        self.bic = -83.09027
        self.llf = -163.5539382 # from Stata, same as ours with scale = 1
        self.llf_R = -82.47352  # Very close to ours as is
        self.scale = 0.003584283
        self.pearsonX2 = .0860228056
        self.resids = glm_test_resids.scotvote_resids

class star98(object):
    def __init__(self):
        self.params = (-0.0168150366,  0.0099254766, -0.0187242148,
            -0.0142385609, 0.2544871730,  0.2406936644,  0.0804086739,
            -1.9521605027, -0.3340864748, -0.1690221685,  0.0049167021,
            -0.0035799644, -0.0140765648, -0.0040049918, -0.0039063958,
            0.0917143006,  0.0489898381,  0.0080407389,  0.0002220095,
            -0.0022492486, 2.9588779262)
        self.bse = (4.339467e-04, 6.013714e-04, 7.435499e-04, 4.338655e-04,
            2.994576e-02, 5.713824e-02, 1.392359e-02, 3.168109e-01,
            6.126411e-02, 3.270139e-02, 1.253877e-03, 2.254633e-04,
            1.904573e-03, 4.739838e-04, 9.623650e-04, 1.450923e-02,
            7.451666e-03, 1.499497e-03, 2.988794e-05, 3.489838e-04,
            1.546712e+00)
        self.null_deviance = 34345.3688931
        self.df_null = 302
        self.deviance = 4078.76541772
        self.df_resid = 282
        self.df_model = 20
        self.aic_R = 6039.22511799
        self.aic_Stata = 19.93144
        self.bic = 2467.494
        self.llf = -2998.612928
        self.scale = 1.
        self.pearsonX2 = 4051.921614
        self.resids = glm_test_resids.star98_resids

class inv_gauss():
    '''
    Data was generated by Hardin and Hilbe using Stata.
    Note only the first 5000 observations are used because
    the models code currently uses np.eye.
    '''
#        np.random.seed(54321)
#        x1 = np.abs(stats.norm.ppf((np.random.random(5000))))
#        x2 = np.abs(stats.norm.ppf((np.random.random(5000))))
#        X = np.column_stack((x1,x2))
#        X = add_constant(X)
#        params = np.array([.5, -.25, 1])
#        eta = np.dot(X, params)
#        mu = 1/np.sqrt(eta)
#        sigma = .5
#       This isn't correct.  Errors need to be normally distributed
#       But Y needs to be Inverse Gaussian, so we could build it up
#       by throwing out data?
#       Refs: Lai (2009) Generating inverse Gaussian random variates by
#        approximation
# Atkinson (1982) The simulation of generalized inverse gaussian and
#        hyperbolic random variables seems to be the canonical ref
#        Y = np.dot(X,params) + np.random.wald(mu, sigma, 1000)
#        model = GLM(Y, X, family=models.family.InverseGaussian(link=\
#            models.family.links.identity))

    def __init__(self):
        # set up data #
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
            "inv_gaussian.csv")
        data=np.genfromtxt(filename, delimiter=",", skiprows=1)
        self.endog = data[:5000,0]
        self.exog = data[:5000,1:]
        self.exog = tools.add_constant(self.exog)
        # Results
#NOTE: loglikelihood difference in R vs. Stata vs. Models
# is the same situation as gamma
        self.params = (0.4519770, -0.2508288, 1.0359574)
        self.bse = (0.03148291, 0.02237211, 0.03429943)
        self.null_deviance = 1520.673165475461
        self.df_null = 4999
        self.deviance = 1423.943980407997
        self.df_resid = 4997
        self.df_model = 2
        self.aic_R = 5059.41911646446
        self.aic_Stata = 1.55228
        self.bic = -41136.47
        self.llf = -3877.700354 # same as ours with scale set to 1
        self.llf_R = -2525.70955823223  # this is close to our defintion
        self.scale = 0.2867266359127567
        self.pearsonX2 = 1432.771536
        self.resids = glm_test_resids.invgauss_resids


### REGRESSION MODEL RESULTS : OLS, GLS, WLS, AR###

class longley(object):
    '''
    The results for the Longley dataset were obtained from NIST

    http://www.itl.nist.gov/div898/strd/general/dataarchive.html

    Other results were obtained from Stata
    '''
    def __init__(self):
        self.params = ( 15.0618722713733, -0.358191792925910E-01,
                 -2.02022980381683, -1.03322686717359, -0.511041056535807E-01,
                 1829.15146461355, -3482258.63459582)
        self.bse = (84.9149257747669, 0.334910077722432E-01,
                   0.488399681651699, 0.214274163161675, 0.226073200069370,
                   455.478499142212, 890420.383607373)
        self.conf_int = [(-177.0291,207.1524),
                   (-.111581,.0399428),(-3.125065,-.9153928),
                   (-1.517948,-.5485049),(-.5625173,.4603083),
                   (798.7873,2859.515),(-5496529,-1467987)]
        self.scale = 92936.0061673238
        self.rsquared = 0.995479004577296
        self.rsquared_adj = 0.99246501
        self.df_model = 6
        self.df_resid = 9
        self.ess = 184172401.944494
        self.ssr = 836424.055505915
        self.mse_model = 30695400.3240823
        self.mse_resid = 92936.0061673238
        self.fvalue = 330.285339234588
        self.llf = -109.6174
        self.aic = 233.2349
        self.bic = 238.643
        self.pvalues = np.array([ 0.86314083,  0.31268106,  0.00253509,
            0.00094437,  0.8262118 , 0.0030368 ,  0.0035604 ])
#pvalues from rmodelwrap
        self.resid = np.array((267.34003, -94.01394, 46.28717, -410.11462,
            309.71459, -249.31122, -164.04896, -13.18036, 14.30477, 455.39409,
            -17.26893, -39.05504, -155.54997, -85.67131, 341.93151,
            -206.75783))

#    sas_bse_HC0=(51.22035, 0.02458, 0.38324, 0.14625, 0.15821,
#                428.38438, 832212,)
#    sas_bse_HC1=(68.29380, 0.03277, 0.51099, 0.19499, 0.21094,
#                571.17917, 1109615)
#    sas_bse_HC2=(67.49208, 0.03653, 0.55334, 0.20522, 0.22324,
#                617.59295, 1202370)
#    sas_bse_HC3=(91.11939, 0.05562, 0.82213, 0.29879, 0.32491,
#                922.80784, 1799477)

class longley_gls(object):
    '''
    The following results were obtained from running the test script with R.
    '''
    def __init__(self):
        self.params = (6.738948e-02, -4.742739e-01, 9.489888e+04)
        self.bse = (1.086675e-02, 1.557265e-01, 1.415760e+04)
#FIXME: I don't think the standard errors are taken from the correct
# covariance matrix.  Decide how to get whitened residuals and
# fix

### RLM MODEL RESULTS ###

def _shift_intercept(arr):
    """
    A convenience function to make the SAS covariance matrix
    compatible with stats.models.rlm covariance
    """
    side = np.sqrt(len(arr))
    arr = np.array(arr).reshape(side,side)
    tmp = np.zeros((side,side))
    tmp[:-1,:-1] = arr[1:,1:]
    tmp[-1,-1] = arr[0,0]
    tmp[-1,:-1] = arr[0,1:]
    tmp[:-1,-1] = arr[1:,0]
    return tmp

class huber(object):
    huber_h1 = [95.8813, 0.19485, -0.44161, -1.13577, 0.1949, 0.01232,
            -0.02474, -0.00484, -0.4416, -0.02474, 0.09177, 0.00001, -1.1358,
            -0.00484, 0.00001, 0.01655]
    h1 = _shift_intercept(huber_h1)

    huber_h2 = [82.6191, 0.07942, -0.23915, -0.95604, 0.0794, 0.01427,
            -0.03013, -0.00344, -0.2392, -0.03013, 0.10391, -0.00166, -0.9560,
            -0.00344, -0.00166, 0.01392]
    h2 = _shift_intercept(huber_h2)

    huber_h3 = [70.1633, -0.04533, -0.00790, -0.78618, -0.0453, 0.01656,
            -0.03608, -0.00203, -0.0079, -0.03608,  0.11610, -0.00333, -0.7862,
            -0.00203, -0.00333,  0.01138]
    h3 = _shift_intercept(huber_h3)

class hampel(object):
    hampel_h1 = [141.309,  0.28717, -0.65085, -1.67388, 0.287,  0.01816,
            -0.03646, -0.00713, -0.651, -0.03646,  0.13524,  0.00001, -1.674,
            -0.00713, 0.00001,  0.02439]
    h1 = _shift_intercept(hampel_h1)

    hampel_h2 = [135.248,  0.18207, -0.36884, -1.60217, 0.182, 0.02120,
            -0.04563, -0.00567, -0.369, -0.04563,  0.15860, -0.00290, -1.602,
            -0.00567, -0.00290, 0.02329]
    h2 = _shift_intercept(hampel_h2)

    hampel_h3 = [128.921,  0.05409, -0.02445, -1.52732, 0.054,  0.02514,
            -0.05732, -0.00392, -0.024, -0.05732,  0.18871, -0.00652, -1.527,
            -0.00392, -0.00652,  0.02212]
    h3 = _shift_intercept(hampel_h3)

class bisquare(object):
    bisquare_h1 = [90.3354,  0.18358, -0.41607, -1.07007, 0.1836, 0.01161,
            -0.02331, -0.00456, -0.4161, -0.02331,  0.08646, 0.00001, -1.0701,
            -0.00456, 0.00001,  0.01559]
    h1 = _shift_intercept(bisquare_h1)

    bisquare_h2 = [67.82521, 0.091288, -0.29038, -0.78124, 0.091288,
            0.013849, -0.02914, -0.00352, -0.29038, -0.02914, 0.101088, -0.001,
            -0.78124, -0.00352,   -0.001, 0.011766]
    h2 = _shift_intercept(bisquare_h2)

    bisquare_h3 = [48.8983, 0.000442, -0.15919, -0.53523, 0.000442,
            0.016113, -0.03461, -0.00259, -0.15919, -0.03461, 0.112728,
            -0.00164, -0.53523, -0.00259, -0.00164, 0.008414]
    h3 = _shift_intercept(bisquare_h3)

class andrews(object):
    andrews_h1 = [87.5357, 0.177891, -0.40318, -1.03691, 0.177891,  0.01125,
            -0.02258, -0.00442, -0.40318, -0.02258, 0.083779, 6.481E-6,
            -1.03691, -0.00442, 6.481E-6,  0.01511]
    h1 = _shift_intercept(andrews_h1)

    andrews_h2 = [66.50472,  0.10489,  -0.3246, -0.76664, 0.10489, 0.012786,
            -0.02651,  -0.0036, -0.3246, -0.02651,  0.09406, -0.00065,
            -0.76664,  -0.0036, -0.00065, 0.011567]
    h2 = _shift_intercept(andrews_h2)

    andrews_h3 = [48.62157, 0.034949, -0.24633, -0.53394, 0.034949, 0.014088,
                -0.02956, -0.00287, -0.24633, -0.02956, 0.100628, -0.00104,
                -0.53394, -0.00287, -0.00104, 0.008441]
    h3 = _shift_intercept(andrews_h3)

    resid = [2.503338458, -2.608934536, 3.5548678338, 6.9333705014,
            -1.768179527, -2.417404513, -1.392991531, -0.392991531,
            -1.704759385,-0.244545418, 0.7659115325, 0.3028635237,
            -3.019999429,-1.434221475,2.1912017882, 0.8543828047,
            -0.366664104,0.4192468573,0.8822948661,1.5378731634,
            -10.44592783]

    sresids = [1.0979293816, -1.144242351, 1.5591155202, 3.040879735,
            -0.775498914, -1.06023995, -0.610946684, -0.172360612,
            -0.747683723, -0.107254214, 0.3359181307, 0.1328317233,
            -1.324529688, -0.629029563, 0.9610305856, 0.3747203984,
            -0.160813769, 0.1838758324, 0.3869622398, 0.6744897502,
            -4.581438458]

    weights = [0.8916509101, 0.8826581922, 0.7888664106, 0.3367252734,
            0.9450252405, 0.8987321912, 0.9656622, 0.9972406688,
            0.948837669, 0.9989310017, 0.9895434667, 0.998360628,
            0.8447116551, 0.9636222149, 0.916330067, 0.9869982597,
            0.9975977354, 0.9968600162, 0.9861384742, 0.9582432444, 0]

    conf_int = [(0.7203,1.1360),(.0819,1.2165),(-.3532,.1287),
                (-60.6305,-23.9555)]

    def __init__(self):
        self.params = [0.9282, 0.6492, -.1123,-42.2930]
        self.bse = [.1061, .2894, .1229, 9.3561]
        self.scale = 2.2801
        self.df_model = 3.
        self.df_resid = 17.
        self.bcov_unscaled = []
        self.h1 = self.h1
        self.h2 = self.h2
        self.h3 = self.h3


### RLM Results with Huber's Proposal 2 ###
### Obtained from SAS ###

class huber_huber(object):
    def __init__(self):
        self.h1 = [114.4936, 0.232675, -0.52734, -1.35624, 0.232675, 0.014714,
                -0.02954, -0.00578, -0.52734, -0.02954, 0.10958, 8.476E-6,
                -1.35624, -0.00578, 8.476E-6, 0.019764]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [103.2876, 0.152602, -0.33476, -1.22084, 0.152602, 0.016904,
                -0.03766, -0.00434, -0.33476, -0.03766, 0.132043, -0.00214,
                -1.22084, -0.00434, -0.00214, 0.017739]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [ 91.7544, 0.064027, -0.11379, -1.08249, 0.064027, 0.019509,
                -0.04702, -0.00278, -0.11379, -0.04702, 0.157872, -0.00462,
                -1.08249, -0.00278, -0.00462, 0.015677]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [2.909155172, -2.225912162, 4.134132661, 6.163172632,
                -1.741815737, -2.789321552, -2.02642336, -1.02642336,
                -2.593402734, 0.698655, 1.914261011, 1.826699492, -2.031210331,
                -0.592975466, 2.306098648, 0.900896645, -1.037551854,
                -0.092080512, -0.004518993, 1.471737448, -8.498372406]
        self.sresids = [0.883018497, -0.675633129, 1.25483702, 1.870713355,
                -0.528694904, -0.84664529, -0.615082113, -0.311551209,
                -0.787177874, 0.212063383, 0.581037374, 0.554459746,
                -0.616535106, -0.179986379, 0.699972205, 0.273449972,
                -0.314929051, -0.027949281, -0.001371654, 0.446717797,
                -2.579518651]
        self.weights = [1, 1, 1, 0.718977066, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 0.52141511]
        self.conf_int = [(0.5612,1.0367),(.3987,1.6963),
                (-.4106,.1405),(-62.0611,-20.1172)]
        self.params = (.7990,1.0475,-0.1351,-41.0892)
        self.bse = (.1213,.3310,.1406,10.7002)
        self.scale = 3.2946
        self.df_model = 3
        self.df_resid = 17


class hampel_huber(object):
    def __init__(self):
        self.h1 = [147.4727, 0.299695, -0.67924, -1.7469, 0.299695, 0.018952,
                -0.03805, -0.00744, -0.67924, -0.03805, 0.141144, 0.000011,
                -1.7469, -0.00744, 0.000011, 0.025456]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [141.148, 0.190007, -0.38493, -1.67206, 0.190007, 0.02213,
                -0.04762, -0.00592, -0.38493, -0.04762, 0.165518, -0.00303,
                -1.67206, -0.00592, -0.00303, 0.024301]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [134.5444, 0.05645, -0.02552, -1.59394, 0.05645, 0.026232,
                -0.05982, -0.00409, -0.02552, -0.05982, 0.196946, -0.0068,
                -1.59394, -0.00409, -0.0068, 0.023083]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.125725599, -2.022218392, 4.434082972, 5.753880172,
                -1.744479058, -2.995299443, -2.358455878, -1.358455878,
                -3.068281354, 1.150212629, 2.481708553, 2.584584946,
                -1.553899388, -0.177335865, 2.335744732, 0.891912757,
                -1.43012351, -0.394515569, -0.497391962, 1.407968887,
                -7.505098501]
        self.sresids = [0.952186413, -0.616026205, 1.350749906, 1.752798302,
                -0.531418771, -0.912454834, -0.718453867, -0.413824947,
                -0.934687235, 0.350388031, 0.756000196, 0.787339321,
                -0.473362692, -0.054021633, 0.711535395, 0.27170242,
                -0.43565698, -0.120180852, -0.151519976, 0.428908041,
                -2.28627005]
        self.weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 0.874787298]
        self.conf_int = [(0.4619,1.0016),(.5145,1.9872),
                (-.4607,.1648),(-64.0727,-16.4697)]
        self.params = (.7318,1.2508,-0.1479,-40.2712)
        self.bse = (.1377, .3757, .1596, 12.1438)
        self.scale = 3.2827
        self.df_model = 3
        self.df_resid = 17

class bisquare_huber(object):
    def __init__(self):
        self.h1 = [129.9556, 0.264097, -0.59855, -1.5394, 0.264097,
                0.016701, -0.03353, -0.00656, -0.59855, -0.03353,
                0.124379, 9.621E-6, -1.5394, -0.00656, 9.621E-6, 0.022433]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [109.7685, 0.103038, -0.25926, -1.28355, 0.103038, 0.0214,
                -0.04688, -0.00453, -0.25926, -0.04688, 0.158535, -0.00327,
                -1.28355, -0.00453, -0.00327, 0.018892]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [91.80527, -0.09171, 0.171716, -1.05244, -0.09171,
                0.027999, -0.06493, -0.00223, 0.171716, -0.06493, 0.203254,
                -0.0071, -1.05244, -0.00223, -0.0071, 0.015584]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.034895447, -2.09863887, 4.229870063, 6.18871385,
            -1.715906134, -2.763596142, -2.010080245, -1.010080245,
            -2.590747917, 0.712961901, 1.914770759, 1.82892645, -2.019969464,
            -0.598781979, 2.260467209, 0.859864256, -1.057306197, -0.122565974,
            -0.036721665, 1.471074632, -8.432085298]
        self.sresids = [0.918227061, -0.634956635, 1.279774287, 1.872435025,
            -0.519158394, -0.836143718, -0.608162656, -0.305606249, -0.78384738,                     0.215711191, 0.579326161, 0.553353415, -0.611154703, -0.181165324,
            0.683918836, 0.26015744, -0.319894764, -0.037083121, -0.011110375,
            0.445083055, -2.551181429]
        self.weights = [0.924649089, 0.963600796, 0.856330585, 0.706048833,
            0.975591792, 0.937309703, 0.966582366, 0.991507994, 0.944798311,
            0.995764589, 0.969652425, 0.972293856, 0.966255569, 0.997011618,
            0.957833493, 0.993842376, 0.990697247, 0.9998747, 0.999988752,
            0.982030803, 0.494874977]
        self.conf_int = [(0.5399,1.0465),(.3565,1.7389),
                (-.4271,.1600),(-63.2381,-18.5517)]
        self.params = (.7932, 1.0477, -0.1335, -40.8949)
        self.bse = (.1292, .3527, .1498, 11.3998)
        self.scale = 3.3052
        self.df_model = 3
        self.df_resid = 17


class andrews_huber(object):
    def __init__(self):
        self.h1 = [129.9124, 0.264009, -0.59836, -1.53888, 0.264009,
                0.016696, -0.03352, -0.00656, -0.59836, -0.03352, 0.124337,
                9.618E-6, -1.53888, -0.00656, 9.618E-6, 0.022425]
        self.h1 = _shift_intercept(self.h1)
        self.h2 = [109.7595, 0.105022, -0.26535, -1.28332, .105022, 0.021321,
                -0.04664, -0.00456, -0.26535, -0.04664, 0.157885, -0.00321,
                -1.28332, -0.00456, -0.00321, 0.018895]
        self.h2 = _shift_intercept(self.h2)
        self.h3 = [91.82518, -0.08649, 0.155965, -1.05238, -0.08649, 0.027785,
                -0.06427, -0.0023, 0.155965, -0.06427, 0.201544, -0.00693,
                -1.05238, -0.0023, -0.00693, 0.015596]
        self.h3 = _shift_intercept(self.h3)
        self.resid = [3.040515104, -2.093093543, 4.235081748, 6.188729166,
                -1.714119676, -2.762695255, -2.009618953, -1.009618953,
                -2.591649784, 0.715967584, 1.918445405, 1.833412337,
                -2.016815123, -0.595695587, 2.260536347, 0.859710406,
                -1.059386228, -0.1241257, -0.039092633, 1.471556455,
                -8.424624872]
        self.sresids = [0.919639919, -0.633081011, 1.280950793, 1.871854667,
                -0.518455862, -0.835610004, -0.607833129, -0.305371248,
                -0.783875269, 0.216552902, 0.580256606, 0.554537345,
                -0.610009696, -0.180175208, 0.683726076, 0.260029627,
                -0.320423952, -0.037543293, -0.011824031, 0.445089734,
                -2.548127888]
        self.weights = [0.923215335, 0.963157359, 0.854300342, 0.704674258,
                0.975199805, 0.936344742, 0.9660077, 0.991354016, 0.943851708,
                0.995646409, 0.968993767, 0.971658421, 0.965766352, 0.99698502,
                0.957106815, 0.993726436, 0.990483134, 0.999868981, 0.999987004,
                0.981686004, 0.496752113]
        self.conf_int = [(0.5395,1.0460),(.3575,1.7397),
                (-.4271,.1599),(-63.2213,-18.5423)]
        self.params = (.7928, 1.0486, -0.1336, -40.8818)
        self.bse = (.1292, .3526, .1498, 11.3979)
        self.scale = 3.3062
        self.df_model = 3
        self.df_resid = 17