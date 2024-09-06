```python
def move_one_ball(arr):
    # If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Track whether any elements have moved positions
    moved = False 

    # Iterate through the array and move balls to the correct position
    for i in range(len(arr)):
        # If the ball is in the wrong position, move it
        if arr[i] != i + 1:
            arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
            moved = True

    # If any moves were made, the array is sorted
    return moved == False
```

This approach uses a single loop to move each ball to its correct position. The 'moved' variable is used to track if any elements were moved, which can then be used to determine if the array is sorted. If any moves occurred, it means the array is now sorted in non-decreasing order.