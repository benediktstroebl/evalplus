```python
def monotonic(lst: list) -> bool:
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
        if lst[i] > lst[i + 1]:
            increasing = False
    
    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

In this script, we define a function `monotonic` that takes a list of numbers as input and returns a boolean indicating whether the list is monotonically increasing or decreasing. We initialize two flags, `increasing` and `decreasing`, to `True`, assuming that the list is initially increasing and decreasing. Then we iterate over the list, checking each pair of adjacent elements. If an element is greater than its successor, we set `increasing` to `False`. If an element is less than its successor, we set `decreasing` to `False`. Finally, we return `True` if either `increasing` or `decreasing` is still `True`, indicating that the list is monotonically increasing or decreasing. Otherwise, we return `False`.