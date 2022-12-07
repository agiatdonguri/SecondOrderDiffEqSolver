from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

def f(u, x):
    return (u[1], -5 * u[1] - 7)
    
y0 = [0, 0] # initial conditions

xs = np.arange(0, 10, 0.0001)
us = odeint(f, y0, xs)
ys = us[:, 0]

plt.plot(xs, ys, '-')
plt.plot(xs, ys, 'ro')
plt.xlabel('t')
plt.ylabel('theta')
plt.title('gg ez')
plt.show()
