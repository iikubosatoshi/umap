import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.special

def voigt(xval,params):
    norm,center,lw,gw = params
    z = (xval - center + 1j*lw)/(gw * np.sqrt(2.0))
    w = scipy.special.wofz(z)
    model_y = norm * (w.real)/(gw * np.sqrt(2.0*np.pi))
    return model_y