from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
import math

q = 1.5 * math.pow(10, -9)
V = 7984.03193613
d = 0.176
b = 1
L = 0.165
m = 0.00038
g = 9.8


Fe = q * V / d# + k * q * q / math.pow((d /2 - x), 2)

def f(u, x):
    return (u[1], -b * u[1] / m + Fe * math.cos(u[0]) / m / L - g * math.sin(u[0]) / L)
    
y0 = [0, 0] # initial conditions

xs = np.arange(0, 15, 0.001)
us = odeint(f, y0, xs)
ys = us[:, 0]

plt.plot(xs, ys, '-')
plt.plot(xs, ys, 'ro')
plt.xlabel('t')
plt.ylabel('theta')
plt.title('gg ez')
plt.show()

