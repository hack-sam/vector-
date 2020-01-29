#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
M = np.array([[1,1],[-2,2],[4,-7]])

print("vector:1")
print(M[0,:])
# print("vector:2")
# print(M[1,:])
rows,cols = M.T.shape
print(cols)

for i,l in enumerate(range(0,cols)):
    print("Iteration: {}-{}".format(i,l))
    print("vector:{}".format(i))
    print(M[i,:])
    v1 = [0,0],[M[i,0],M[i,1]]
    # v1 = [M[i,0]],[M[i,1]]
    print(v1)
    plt.figure(i)
    plt.plot(v1)
    plt.show()

