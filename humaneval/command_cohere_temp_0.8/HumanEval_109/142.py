Here's a Python script that includes a function `move_one_ball(arr)` that solves the problem as described in the code block you provided:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array and remove duplicates (assuming unique elements).
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Find the index of the last element in the original array.
    last_index = arr.index(sorted_arr[-1]) if sorted_arr[-1] in arr else -1

    # Determine the maximum number of right shifts needed.
    max_shifts = last_index + 1

    # Iterate through the shifts and check if the target order is achievable.
    for shifts in range(max_shifts + 1):
        shifted_arr = [x for ind, x in enumerate(arr) if ind != shifts] + arr[:shifts]
        if sorted_arr == shifted_arr:
            return True

    # If no suitable shift could achieve the target order, return False.
    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Should print True
print(move_one_ball([3, 5, 4, 1, 2]))  # Should print False
```

This script includes the `move_one_ball()` function, which takes an unsorted list as input and returns `True` if the list can be sorted in non-decreasing order by performing right shifts, and `False` otherwise. Test cases are also provided to validate the function.