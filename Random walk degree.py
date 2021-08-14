# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 07:08:35 2021

@author: TRIPT
"""

import math
import matplotlib.pyplot as plt
import random
import imageio
import time
import os
import numpy as np

np.ax=[]
np.by=[]
filenames=[]
r=3
def random_walk(n):
    x=0
    y=0
    for i in range(n):
        step = random.randrange(0,360,1)
        angle = math.radians(step)
        
        x = x + r*math.cos(angle)
        y = y + r*math.sin(angle)
        np.ax.append(x)
        np.by.append(y)
        
    
    plt.plot(x,y,'.k')
    plt.show()
    return (x,y)
n = 100

for j in range (10):
    random_walk(n)
    for i in range (n-1):
    
        plt.xlim(-(r)*(1.5)*math.sqrt(n), (r)*(1.5)*math.sqrt(n))
        plt.ylim(-(r)*(1.5)*math.sqrt(n), (r)*(1.5)*math.sqrt(n))
   
        plt.plot([np.ax[a] for a in range(0,i+1)],[np.by[a] for a in range(0,i+1)],'-b')
        plt.plot(np.ax[i],np.by[i],'.r')

        filename = f'{i}.png' 
        filenames.append(filename)
    
    # save frame
        plt.savefig(filename)
        plt.close()
    
    
    
    
# build gif
with imageio.get_writer('mygifdont.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)
print('done!!') 
    



