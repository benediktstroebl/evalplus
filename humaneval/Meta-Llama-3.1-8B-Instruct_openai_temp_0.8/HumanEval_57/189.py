```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of elements.
    
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
    
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        if l[i] > l[i + 1]:
            increasing = False
    
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This Python function `monotonic` takes a list `l` as input and returns `True` if the list is either monotonically increasing or decreasing. If the list is neither increasing nor decreasing, the function returns `False`. The function uses two flags `increasing` and `decreasing` to track whether the list is increasing or decreasing respectively. It iterates over the list, and if it finds a pair of elements where the first is greater than the second, it sets `increasing` to `False`. Similarly, if it finds a pair of elements where the first is less than the second, it sets `decreasing` to `False`. The function returns `True` if either `increasing` or `decreasing` is `True`, indicating that the list is either increasing or decreasing.