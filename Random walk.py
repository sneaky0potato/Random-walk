#!/usr/bin/env python
# coding: utf-8

# In[35]:


import random
import math
import matplotlib.pyplot as plt
def random_walk(n):
    x=0
    y=0
    
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y=y+1
        elif step == 'S':
            y=y-1
        elif step == 'E':
            x=x+1
        elif step == 'W':
            x=x-1
    return (x,y)
xvalues = []
yvalues = []
for i in range (1000):
    walk = random_walk(10000)
    (x,y) = random_walk(10000)
    xvalues.append(x)
    yvalues.append(y)
plt.plot(xvalues,yvalues,'.b')
plt.show()


# In[ ]:





# In[ ]:




