# -- coding: utf-8 --
"""
Created on Sun Aug 15 10:04:54 2021

@author: Ranjan
"""

import math
import matplotlib.pyplot as plt
import random
import imageio
import time
import os

r=3 
n = 500
m = 3
ax=[[0],[0],[0]]
by=[[0],[0],[0]]

filenames=[]

def random_walk(n,m):

    j = 0
    for j in range(m):
      x=0
      y=0
      for i in range(n):
        step = random.randrange(0,360,1)
        angle = math.radians(step)
        distance = math.sqrt(x**2+y**2)

        x = x + (r)/(1+distance/10)*math.cos(angle)
        y = y + (r)/(1+distance/10)*math.sin(angle)
        
        ax[j].append(x)
        by[j].append(y)
    plt.plot(x,y,'.k')
    plt.show()
    return (x,y)


random_walk(n,m)
for i in range(m):
    print (ax[i], '\n')
    print (by[i], '\n')
for i in range (n-1):

    plt.xlim(-(r)*(1.5)*math.sqrt(n), (r)*(1.5)*math.sqrt(n))
    plt.ylim(-(r)*(1.5)*math.sqrt(n), (r)*(1.5)*math.sqrt(n))
    #plt.xlim(-5*math.log(n), 5*math.log(n)) #fix plot
    #plt.ylim(-5*math.log(n),5*math.log(n))
    #plt.plot([ax[b][a]for b in range(0,m) for a in range(0,i+1)],[by[a][b] for a in range(0,m) for b in range(0,i+1)],'-b')
    #plt.plot([ax[a][i] for a in range (0,m)],[by[a][i] for a in range (0,m)],'.r')
    plt.plot([ax[i][0],ax[i+1][0],ax[i][1],ax[][i+1],ax[2][i],ax[2][i+1]] ,'-r')

    '''for a in range (0,m):
        #plt.plot([ax[a][b] for b in range(0,i+1)],[by[a][b] for b in range(0,i+1)],'-b')
        plt.plot(ax[a][i] ,by[a][i],'.r')'''

    filename = f'{i}.png' 
    filenames.append(filename)

# save frame
    plt.savefig(filename)
    plt.close()




# build gif
with imageio.get_writer('mygifwhy.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files
for filename in set(filenames):
    os.remove(filename)
print('done!!')