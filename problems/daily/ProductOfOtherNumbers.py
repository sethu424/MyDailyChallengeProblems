'''
Created on 28-Oct-2018
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

@author: sethu
'''
from partd.utils import suffix

def products(arr):
    '''
    Approach: To compute the ith element simply needs the product of numbers before i and the product of numbers after i. 
    Then we could multiply those two numbers to get our desired product.
    '''
    
    #Create prefix products
    prefix_products = []
    for num in arr:
        if prefix_products:
            prefix_products.append(prefix_products[-1]*num)
        else:
            prefix_products.append(num)

    #Create suffix products
    suffix_products = []
    for num in reversed(arr):   #reversed returns a "reversed" iterator on the input list
        if suffix_products:
            suffix_products.append(suffix_products[-1]*num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
    
    #Generate result
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(suffix_products[i+1]) 
        elif i == len(arr)-1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    return result
        
        
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(products(arr))