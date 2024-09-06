```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required.
    """
    # Ensure the array contains only unique integers.
    arr = list(set(arr))
    # Create a reversed copy of the array.
    rev_arr = arr[::-1]
    # Calculate the absolute difference between the two arrays.
    diff = [abs(x-y) for x, y in zip(arr, rev_arr)]
    return sum(diff) // 2
```

The function works by first removing any duplicate elements in the input array using `set()`. Then, it creates a reversed copy of the unique array and calculates the absolute difference between the two arrays. Finally, it returns the average of the difference, which provides the minimum number of changes required to make the original array palindromic.