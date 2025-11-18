from fitting_functions import *
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import norm
data = np.loadtxt('tips.csv', delimiter=",", dtype=str)
x = data[1:,0].astype(np.float32)
y = data [1:,1].astype(np.float32)
print('y=',y)
print('x=',x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = round(params[0],2)
intercept = round(params[1],2)
print(slope)
print(intercept)



print_equation(slope,intercept,'dollars','dollars')

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("dollars") #change the units as appropriate
plt.ylabel("dollars")  #change the units as appropriate
plt.show()

x = data[1:, 0].astype(np.float32)
y = data[1:, 6].astype(np.float32)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = round(params[0],2)
intercept = round(params[1],2)
print(slope)
print(intercept)
print_equation(slope,intercept,'dollars','%')

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("dollars") #change the units as appropriate
plt.ylabel("%")  #change the units as appropriate
plt.show()
