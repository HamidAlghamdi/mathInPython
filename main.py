
import sympy as smp

x=smp.symbols('x', real=True)
f=smp.sin(x)**3 * smp.exp(-5*x)
print(f)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc

# Define the function and its derivative
def f(x):
    return x**2

def df(x):
    return 2*x

# Create the function for the tangent line
def tangent_line(x, x1):
    y1 = f(x1)
    return df(x1)*(x - x1) + y1

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 400)
ax.plot(x, f(x), 'b-', label='y = x^2')
line, = ax.plot([], [], 'r-', linewidth=2, label='Tangent')
point, = ax.plot([], [], 'go')

# Initialization function for the animation
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Update function for the animation
def update(frame):
    x1 = np.linspace(-10, 10, 400)[frame]
    y1 = f(x1)
    y_tangent = tangent_line(x, x1)
    
    line.set_data(x, y_tangent)
    point.set_data(x1, y1)
    return line, point

ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, repeat=True)

plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 100)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$Tangent to y = \frac{cos} {(\pi)}x^2$') #The $ is to convert to math standard form, for pi, just precede them with back slash
# use \frac{nemurator}{denominator}
plt.grid()
title='tangent_animation'
ani.save(f'animations/{title}.gif')
plt.show()
