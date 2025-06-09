import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

## Defining our system of differential equations...
## Define function that returns differential change in position due to gravity

def gravity(t, x, masses):

    ## Will have form x = [x, y, v_x, v_y]
    ## This assumes no z motion

    ## Calculating distance:
    r = np.sqrt((x[0])**2 + (x[1])**2)

    ## v = dx/dt
    dx[0] = x[2]
    dx[1] = x[3]

    ## Now using Newton's gravitational force:
    dx[2] = masses * (x[0]) / r**3
    dx[3] = masses * (x[1]) / r**3

    return dx

