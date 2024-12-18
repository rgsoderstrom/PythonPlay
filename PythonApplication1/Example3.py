
# Tutorial 5, Installing Packages


from math import radians
import numpy as np                # installed with matplotlib
import matplotlib.pyplot as plt

def main():
   x = np.arange(0, radians(1800), radians(12))
   plt.plot(x, np.sinc(x), 'r')
   plt.show()


main()
z = 22 # python -i Example3.py
       # z is visible after plot closed
       #   in WIndows cmdshell, doesn't work in git bash
       

