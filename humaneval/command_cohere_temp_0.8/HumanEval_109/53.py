```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Use a counter to keep track of the number of right shifts required to sort the array.
    shift_count = 0
    
    # Iterate through the array and count the number of elements in the wrong order.
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            shift_count += 1
            if shift_count >= len(arr):
                return False
    
    return True
```

The `move_one_ball()` function analyzes the given array `arr` to determine if a non-decreasing order can be achieved by performing right shift operations. If the array is empty, it returns `True`, since shifting is not needed for an empty array. If not, it iterates through the array, counting the number of elements that are not in the correct order. If the count exceeds the length of the array, it returns `False`, as there aren't enough shifts to arrange the balls in ascending order. Otherwise, it returns `True`, indicating that rearrangement is possible.