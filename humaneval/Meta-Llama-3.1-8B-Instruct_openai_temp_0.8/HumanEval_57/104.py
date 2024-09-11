```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    # Check if the list is empty
    if len(l) == 0:
        return True

    # Check if the list is monotonically increasing
    increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is monotonically decreasing
    decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))

    # Return True if the list is either monotonically increasing or decreasing
    return increasing or decreasing
```

You can run this script to test the `monotonic` function with the provided examples. Note that this function returns `True` for any list that is either monotonically increasing or decreasing, which includes empty lists (since there are no elements to compare). If you want to handle empty lists differently, you can modify the function to return `False` instead of `True`.