```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes required to make the array palindromic
    """
    # Ensure the array contains only unique elements
    arr = list(set(arr))
    # Calculate reverse of array
    rev_arr = sorted(arr)[::-1]
    return sum((x != y for x, y in zip(arr, rev_arr)))
```

The function `smallest_change()` works by first removing any duplicate elements in the input array, as it is easier to manipulate unique elements. It then creates a reverse copy of the array and calculates the differences between the original array and its reverse, which represents the number of changes required to make the array palindromic. Finally, it returns the total number of changes needed.