```python
def move_one_ball(arr):
    # If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts needed.
    # Initialize with the number of elements in the array - 1 (assuming
    # the last element is the largest and would "bubble up" to its correct
    # position with shifts)
    shifts = len(arr) - 1

    # Iterate over the array and compare the element at the end with
    # the element at the beginning. If they are out of order, decrement
    # the counter.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            shifts -= 1

    # If any shifts were needed at all, it's possible to sort with shifts.
    return shifts >= 0
```

This approach uses dynamic programming with a counter to keep track of the number of "bubbles" or elements out of order in the array. It initializes the counter based on the number of elements in the array, and then iterates through the array to compare each element with the next one. If the current element is greater than the next one, it decrement the counter. Finally, if the counter is greater than or equal to zero, it returns True, indicating that the array can be sorted with moves; otherwise, it returns False. 

This solution has a time complexity of O(n), where n is the number of elements in the array, as it requires only a single pass through the input array.