import numpy as np 
import math
import matplotlib.pyplot as mpl 

#math
def add(num1, num2):
    answer = num1 + num2
    return answer

def subtract(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

def remainder(num1, num2):
    answer = num1 % num2
    return answer

def absolute_value(num):
    answer = abs(num)
    return answer

def rad_to_degrees(rad):
    answer = 180/math.pi * rad
    return answer

def degrees_to_rad(degrees):
    answer =  math.pi/180 * degrees
    return answer

def square_root(num):
    if (num >= 0):
        return math.sqrt(num)
    else:
        return pow(num, 0.5)

def flip_sign(num):
    if (num < 0 ):
        return abs(num)
    elif (num == 0):
        return num
    else:
        num = num * -1
        return num

def inverse(num):
    return 1/num

def exponential(num):
    return math.exp(num)

def squared(num):
    return num**2

def factorial(num):
    for i in range(num + 1):
        total *= i
    return total 

def n_root(num, n):
    n = inverse(n)
    answer = pow(num, n)
    return answer

def n_power(num, n):
    answer = num**n
    return answer

def log_10(num):
    answer = math.log10(num)
    return answer

def natural_log (num):
    answer = math.log(num)
    return answer

def n_base_log(num, n):
    answer = math.log(num, n)
    return answer

