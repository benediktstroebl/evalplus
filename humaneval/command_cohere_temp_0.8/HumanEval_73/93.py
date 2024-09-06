```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Create a reversed copy of the array
    rev = arr[::-1]
    # Count number of changes required
    change = 0
    for a, b in zip(arr, rev):
        # If the two elements are not equal, increment the change count
        if a != b:
            change += 1
    return change
```

The `smallest_change` function works by first removing any duplicate elements in the input array using `set()`. It then creates a reversed copy of the unique array. The function counts the number of elements that don't match between the original and reversed copies, incrementing the `change` count for each mismatch. This count ultimately gives the minimum number of changes needed to make the original array palindromic.