from xml import dom
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from functools import partial
from scipy import optimize

def smooth(x):
    return np.sin(2.0*np.pi*x)

ng = 201;
x  = np.linspace(0,1,ng)
h = 1/(ng-1);
u  = smooth(x)
ue = smooth(x)
plot_freq = 1
cfl = 0.9
t = 0.0
# plot initial condition
if plot_freq >0:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1,line2 = ax.plot(x, u, 'ro',x, ue, 'b')
    #line1, = ax.plot(x, u, 'o')
    ax.set_xlabel('x'); ax.set_ylabel('u')
    plt.title('ng='+str(ng)+', CFL='+str(cfl)+', time ='+str(np.round(t,3)))
    plt.legend(('Numerical','Exact'))
    #plt.ylim(0.3,0.7)
    plt.grid(True); plt.draw(); plt.pause(0.1)
    wait = input("Press enter to continue ")

Tf = 1.0; # final time
dt = cfl * h

while t < Tf:
    lam = dt/h
    if t+dt > Tf:
        dt = Tf - t
        lam = dt/h
    # warning! uold = u is a wrong assignment
    uold = np.copy(u)

    for i in range(1, ng):
        u[i] = uold[i] - lam * (uold[i] - uold[i-1])

    u[0] = u[-1];
    t +=dt
    if plot_freq > 0:
        ue = smooth(x-t)
        line1.set_ydata(u)
        line2.set_ydata(ue)
        plt.title('ng='+str(ng)+', CFL='+str(cfl)+', time ='+str(np.round(t,3)))
        plt.draw(); plt.pause(0.1)
    
plt.show()
# u_t + c u_x = 0,  u(x,t ) = g(x-ct)
# u(x,0) = g(x)   