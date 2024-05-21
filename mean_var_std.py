import numpy as np

li= [1,2,3,4,5,6,7,8,9]
def calculate(li):
    a,b,c,d,e,f,g,h,i = li
    arr1 = np.array([[a,b,c], [d,e,f], [g,h,i]])
    dict1 = {'mean': [(arr1.mean(axis=0),arr1.mean(axis=1), arr1.mean())],
            'variance': [arr1.var(axis=0),arr1.var(axis=1), arr1.var()],
            'standard deviation': [arr1.std(axis=0),arr1.std(axis=1), arr1.std()],
            'max': [arr1.max(axis=0),arr1.max(axis=1), arr1.max()],
            'min': [arr1.min(axis=0),arr1.min(axis=1), arr1.min()],
            'sum': [arr1.sum(axis=0),arr1.sum(axis=1), arr1.sum()],
            }
    return dict1


try:
 arr = calculate([1,2,3,4,5,6,7,8,9])
 print(arr)
except ValueError:
   print("List must contain nine numbers.")

