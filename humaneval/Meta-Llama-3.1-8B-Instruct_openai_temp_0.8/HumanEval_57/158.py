```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    
    Example:
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
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This Python script defines a function `monotonic` that checks if a given list is monotonically increasing or decreasing. The function iterates over the list, maintaining two flags: `increasing` and `decreasing`. It sets `increasing` to `False` if it finds an element that is smaller than the next one, and `decreasing` to `False` if it finds an element that is larger than the next one. The function returns `True` if either `increasing` or `decreasing` is `True`, indicating that the list is monotonically increasing or decreasing, respectively.