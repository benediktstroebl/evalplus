Here's a Python script that includes a function `move_one_ball(arr)` that solves the problem as described in the code block you provided:
```python
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be formed by shifting
    return sorted_arr == unique_arr

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Should print True
print(move_one_ball([3, 5, 4, 1, 2]))  # Should print False
```
This script includes the `move_one_ball()` function, which takes an unordered array as input and returns `True` if the non-decreasing order can be achieved by performing right shift operations, and `False` otherwise. It first checks if the array is empty and returns `True` if so. It then sorts the array and compares it with the unique elements in the original array to determine if the desired permutation is possible.