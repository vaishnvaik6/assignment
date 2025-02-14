# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:39:39 2025

@author: vaish
"""

##1]Create a 1D NumPy array with numbers from 1 to 10.
# import numpy as np

# arr1=np.arange(0,11)
# print(arr1)


# ##2]Create a 2D NumPy array of shape (3,3)
# ## with random integers between 10 and 50.
# import numpy as np
# arr=np.random.randint(10,50,(3,3))
# print(arr)
##3]Create a NumPy array of size 5 filled with 
##zeros, ones, and a constant value of 7.                                
# import numpy as np
# arr=np.array([0,1,7,0,1])
# print(arr)
##4]Given an array arr = np.array([10, 20, 30, 40, 50]), retrieve:
## a) The first three elements.
# #b) The last two elements.
# #c) Elements from index 1 to 4 with a step of 2.
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# arr1=arr[0:3]
# last_two= arr[-2:]
# step_elements=arr[1:4:2]
# print("first 3 elements:",arr1)
# print("last 2 elements:",last_two)
# print("elements from index 1 to 4 with step of 2:",step_elements)
##5]Convert a 1D array of 12 elements into a 3x4 matrix.
import numpy as np
arr=np.arange(1,13)
matrix=arr.reshape(3,4)
matrix1=arr.reshape(2,6)
matrix2=arr.reshape(6,2)
print("original array:",arr)
print("2d array(3,4):",matrix)
print("2d array(2,6):",matrix1)
print("2d array(6,2):",matrix2)