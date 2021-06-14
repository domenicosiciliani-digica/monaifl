import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import sys
import os
from pathlib import Path
home = str(Path.home())
import numpy as np
#from scipy.interpolate import make_interp_spline, BSpline
#from scipy.interpolate import CubicSpline
from scipy import interpolate
logpath = os.path.join(home, "monaifl", "trainer", "save","logs","client")
#logName = 'mnistlog.txt'
logName = 'mnistlog.txt'
logFile = os.path.join(logpath, logName)

style.use('seaborn')
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(20, 15))

def animate(i):
    graph_data = open(logFile,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    zs = []
    for line in lines:
        if len(line) > 1:
            x, y, z = line.split(',')
            xs.append(int(x)+1)
            ys.append(float(y))
            zs.append(float(z))
    ax1.clear()
    ax2.clear()

    xn = np.array(xs)
    yn = np.array(ys)
    zn = np.array(zs)

    if (xn.size>1):

        # #define x as 200 equally spaced values between the min and max of original x 
        xnew = np.linspace(xn.min(), xn.max(), 300) 

        # #define spline
        spl1 = interpolate.interp1d(xn, yn)
        spl2 = interpolate.interp1d(xn, zn)
    
        ynew = spl1(xnew)
        znew = spl2(xnew)

        #create smooth line chart 
        ax1.plot(xnew, ynew, color='#444444', label='Model Loss')
        ax2.plot(xnew, znew, color='#2494CC', label='Model Accuracy')

        ax1.legend()
        ax1.set_title("Model Training Monitor", fontsize=20)
        ax1.set_ylabel("Loss", fontsize=16)

        ax2.legend()
        ax2.set_ylabel("Accuracy(%)", fontsize=16)
        ax2.set_xlabel("No of Epochs", fontsize=16)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()
plt.show()