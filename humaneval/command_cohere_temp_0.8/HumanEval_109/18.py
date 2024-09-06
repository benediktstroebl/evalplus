```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Iterate through the array and count the number of shifts required for each element
    for i in range(len(arr)):
        # If the current element is smaller than the next one, it will need to be shifted
        if arr[i] < arr[i+1]:
            shifts += 1

    # Return False if any shifts were required, True otherwise
    return shifts == 0
    """
```

The `move_one_ball()` function implements the logic outlined in the problem statement. It iterates through the array, counting the number of shifts required to sort the array in non-decreasing order. If the count is 0, indicating no shifts are needed, the function returns `True`, indicating that sorting is possible; otherwise, it returns `False`. This algorithm has a time complexity of O(n), where n is the length of the input array.