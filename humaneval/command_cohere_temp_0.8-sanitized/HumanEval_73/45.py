import unittest
def smallest_change(arr):
    # Initialize the result to the length of the array
    result = len(arr)
    
    # Iterate over the array and reduce the result if a pair of identical elements is found
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            result -= 1
    
    # Handle cases where the array has odd or even length respectively
    if len(arr) % 2 == 0:
        result //= 2
    return result