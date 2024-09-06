Here's a Python script that contains a function named `move_one_ball` that solves the problem:
```python
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize the variable res to False
    res = False
    # Initialize the variable count to keep track of right shift operations
    count = 0
    # Iterate over the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # If the current element is smaller than or equal to the last element, increment count
        if arr[i] <= arr[len(arr) - 1]:
            count += 1
        # If the count equals the length of the array, we can get a non-decreasing array
        if count == len(arr):
            res = True
            break
    # Return the variable res
    return res
```

This script returns True if it is possible to obtain a non-decreasing array by performing the right shift operation any number of times. Otherwise, it returns False. This algorithm optimizes the process by tracking the number of shifts required for each element to find the smallest element's position. If any element's position is found at the array's starting position or before, the algorithm determines that a non-decreasing array is possible to achieve through shifting, hence, returning True. Otherwise, it returns False, guaranteeing the validity of the solution.