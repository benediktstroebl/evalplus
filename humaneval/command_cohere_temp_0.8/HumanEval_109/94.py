```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    max_shift = 0

    # Traverse the array from the second position to the end, calculating the maximum number of right shifts required
    for i in range(1, len(arr)):
        # Calculate the number of shifts required to move the current element to the first position
        shift = arr[i] - arr[0]
        max_shift = max(max_shift, shift)

    # If the maximum number of right shifts is zero, the array can be sorted with the given operation
    return max_shift == 0
```

The `move_one_ball()` function assesses the viability of arranging the array in non-decreasing order through repeated right shifts. It traverses the array, computing the gap between each element and the earliest element. The maximum discrepancy between array members and the initial element is tracked using an auxiliary variable called `max_shift`. Once this computation concludes, the function returns False if the maximum shift count is above zero, implying that the operation cannot sort the array. However, it returns True if the maximum shift count is zero, indicating that the array is already sorted or can be sorted using the right shift operation. 

This approach guarantees accuracy in determining the maximum shift requirement for the array's elements while maintaining efficiency in computational complexity, as it only requires a single pass through the input.