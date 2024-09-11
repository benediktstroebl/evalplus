```python
def monotonic(lst: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        lst (list): A list of numbers.
    
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
    
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        elif lst[i] > lst[i + 1]:
            increasing = False
    
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This function works by iterating over the list and keeping track of whether it is increasing or decreasing. If at any point it finds a pair of elements that do not follow the current trend, it sets the corresponding flag to `False`. Finally, it returns `True` if either flag is still `True`, indicating that the list is monotonically increasing or decreasing.