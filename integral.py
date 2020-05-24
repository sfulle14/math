#trapezoidal integral method

from scipy import random 
import numpy as np 
import matplotlib.pyplot as plt 


# limits of integration (a,b)
# number of trapezoids n
def integral(func, a, b, n):
    h = float(b-a)/n
    result = (0.5 * func(a)) + (0.5 * func(b))

    for i in range(1, n):
        result += func(a + i*h)

    result *= h
    return result