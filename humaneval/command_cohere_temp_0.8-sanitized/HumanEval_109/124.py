import unittest
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    
    # Initialize the variable flag to False
    flag = False
    
    # Find the minimum element in the array
    mini = min(arr)
    
    # Check if the minimum element is at the first position
    if arr[0] == mini:
        flag = True
    
    # Iterate over the array to check if any number is greater than the minimum element
    for num in arr:
        if num > mini:
            flag = True
            break
    
    # If the flag is still False after iterations, it is possible to obtain a non-decreasing array
    return flag