```python
def monotonic(l: list) -> bool:
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of integers.
    
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
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 5, 5, 5]))  # True
```

This script defines a function `monotonic` that checks if a list of integers is monotonically increasing or decreasing. It initializes two flags, `increasing` and `decreasing`, to `True`, and then iterates over the list. If it finds an element that is smaller than the previous one, it sets `increasing` to `False`. If it finds an element that is larger than the previous one, it sets `decreasing` to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is still `True`, and `False` otherwise. The test cases at the end check the function with various inputs.