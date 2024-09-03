```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindrommic array is is an array that
    is read the same backwards and forwards.

    Returns: number of changes required to make arr palindromic.
    """
    required number of changes to be stored in a list and returned.
    """
arr = [1, 2, 3, 4, 3, 2, 2, 1]
    # Sort the array
    arr.sort()
    arr.rotate()
    the method.
    for i in arr:
        if arr[::-1][i] != arr[i]:
            return i
    return 0

# Test cases
arr = [1, 2, 3, 4, 3, 2, 2, 1]
test_arr = smallest_change(arr)
print("Test Array:", arr)
print("Changes:", test_arr)
```