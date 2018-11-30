<<<<<<< HEAD
import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    r = np.subtract(np.multiply(np.multiply(alpha, Z), np.power(np.divide(L, K), 1-alpha)), delta)
    return r

alpha = 0.3
Z = 1.0
delta = 0.05
K = 1.0
L = 2.0
r = get_r(K, L, alpha, Z, delta)
print(r)
alpha2 = 0.4
Z2 = 0.5
delta2 = 0.01
K2 = np.array([90.5, 130.2, 141.7, 140.0, 135.8])
L2 = np.array([76.5, 82.2, 85.7, 83.0, 79.8])
r2 = get_r(K2, L2, alpha2, Z2, delta2)
print(r2)
=======
'''
------------------------------------------------------------------------
This module contains the function get_r()
------------------------------------------------------------------------
'''


def get_r(K, L, alpha, Z):
    r = alpha + Z * (L / K) ** alpha

    return r
>>>>>>> upstream/master
