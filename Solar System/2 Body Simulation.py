import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

## Defining our system of differential equations...
## Define function that returns differential change in position due to gravity

def gravity(t, x, masses):

    ## Will have form x = [x, y, v_x, v_y]
    ## This assumes no z motion

    ## Calculating distance:
    r = np.sqrt((x[0])**2 + (x[1])**2)

    dx = np.zeros(4)

    ## v = dx/dt
    dx[0] = x[2]
    dx[1] = x[3]

    ## Now using Newton's gravitational force:
    dx[2] = masses * (x[0]) / r**3
    dx[3] = masses * (x[1]) / r**3

    return dx

## We assume the Sun is at (0,0) in our system
## Masses of bodies is usually quoted in terms of Solar mass ratios - Gaussian Gravitation Constant

## Initial Conditions:

## Gaussian mass:
GM = -(0.01720209895)**2

x = np.zeros(4)

# Will have the form x = [x,y,v_x, v_y]
# Thus we must define an offset position and an initial velocity

x[0] = -1.756895992827094E-01
x[1] = 9.659716383076408E-01
x[2] = -1.22463621150023E-02
x[3] = -3.020684839068507E-03

## We define a timescale that we simulate over (Ten years)

times = [0, 3650.0]


## Time to solve...
sol = solve_ivp(gravity, times, x, args=(GM,), method='RK45', rtol=1e-12, dense_output=True)

sun_pos = [0,0,0]


## Now we can plot 

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(y.y[0][:], y.y[1][:], 'b')
# ## Plotting positions:
# ax.scatter(0,0,0, color='orange', s=100, edgecolors='black')
# ax.scatter(x[0], x[1], 0, color='blue', s=50)
# plt.show()


###### Try with some animation?

fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')

ax.scatter(0,0,0, color='orange', s=100, edgecolors='black')

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-0.1, 0.1)

earth_point, = ax.plot([], [], [], 'bo')

orbit, = ax.plot([], [], [], 'b-', alpha=0.5)

num_frames = 500

def update(frame):
    t = times[0] + (times[1] - times[0]) * frame / num_frames

    pos = sol.sol(t)

    earth_point.set_data([pos[0]], [pos[1]])
    earth_point.set_3d_properties([0])

    orbit.set_data(sol.y[0][:frame], sol.y[1][:frame])
    orbit.set_3d_properties(0)

    return earth_point, orbit

animation = FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)
plt.show()