```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of possible shifts
    shifts = 0

    # Traverse through the array
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            shifts += 1
            if shifts > len(arr) - 1:
                return False

    return True
```

The function uses a counter to keep track of how many shifts are needed to arrange the array in non-decreasing order. If the total number of shifts exceeds the length of the array, it is not possible to achieve this order, and the function returns False. Otherwise, it returns True.