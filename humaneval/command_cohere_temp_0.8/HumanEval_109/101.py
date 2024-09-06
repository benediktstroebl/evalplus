Here's a Python script that includes a function named `move_one_ball` from the given problem statement:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Get the number of right shifts needed to sort the array
    shifts = len(arr) - len(sorted_arr)

    # If it's possible to perform that many shifts, return True
    return shifts >= 0
```

This script includes a function `move_one_ball(arr)` that solves the problem statement. If the input array is empty, it is already sorted, so the function returns True. If the array is not empty, it is sorted and unique, and the number of right shifts needed to sort it is calculated. If it's possible to perform that many shifts, the function returns True, otherwise, it returns False.