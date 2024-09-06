import unittest
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if any element is equal to the last element which indicates a possibility of sorting.
    return arr[-1] == arr[0] and any(x for x in arr[1:-1])