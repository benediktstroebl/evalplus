### Monotonic List Checker

Here's a Python function that checks whether the elements in a list are monotonically increasing or decreasing:

```python
def monotonic(lst: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): The input list to check.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False
    
    return increasing or decreasing
```

### Explanation

This function uses a simple and efficient approach to check whether the list elements are monotonically increasing or decreasing. It initializes two flags, `increasing` and `decreasing`, to `True`. Then, it iterates through the list from the second element to the end. If it finds an element that is smaller than the previous one, it sets `increasing` to `False`. If it finds an element that is larger than the previous one, it sets `decreasing` to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is `True`, indicating that the list is monotonically increasing or decreasing, respectively. If both flags are `False`, it returns `False`, indicating that the list is not monotonically increasing or decreasing.