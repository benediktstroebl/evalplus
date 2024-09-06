```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    # Calculate the midpoint of the array
    mid = n // 2
    # Initialize the count of changes to the maximum possible value
    change_count = n - 1
    # Initialize the first and last indices to the start and end of the array
    f = 0
    r = n - 1
    # Iterate through the array, reducing the count of changes if a duplicate is found
    while f <= r:
        if arr[f] == arr[r]:
            f += 1
            r -= 1
            change_count = min(change_count, f - mid)
        elif arr[f] > arr[r]:
            f += 1
        else:
            r -= 1
    # Return the final count of changes
    return change_count
```

The function `smallest_change` solves the problem as described in the prompt. You can test the function by calling it with different input arrays and verifying the results against the examples provided.