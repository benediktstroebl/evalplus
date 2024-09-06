```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Use a counter to keep track of the number of right shifts required to sort the array.
    shifts = 0
    
    # Traverse the array from the end to the start.
    for i in range(len(arr) - 2, -1, -1):
        # Increment the number of shifts if the current element is smaller than the next element.
        if arr[i] < arr[i + 1]:
            shifts += 1
        # If the number of shifts required is greater than or equal to the length of the array, it is not possible to sort it in non-decreasing order.
        if shifts >= len(arr):
            return False
    
    # If we reach here, it is possible to perform the required number of right shifts to sort the array.
    return True
```

The `move_one_ball()` function evaluates whether it is feasible to sort the array in non-decreasing order using a single ball (element) movement, which entails shifting all elements one position to the right. To do this, it counts the number of necessary shifts to arrange the array in the correct order. If the total number of shifts is greater than or equal to the array's length, it returns `False` since it will not be possible to achieve a sorted arrangement. However, if it is feasible to do so, it returns `True`. 

This approach guarantees that the function correctly determines the viability of sorting for any given input array.