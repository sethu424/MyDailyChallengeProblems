'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Created on 25-Oct-2018

@author: sethu
'''

def isSumK(arr, k):
    reminders = set()
    
    for num in arr:
        if k-num in reminders:
            return True
        reminders.add(num)
        
    return False
if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    k = 17
    print(isSumK(arr, k))