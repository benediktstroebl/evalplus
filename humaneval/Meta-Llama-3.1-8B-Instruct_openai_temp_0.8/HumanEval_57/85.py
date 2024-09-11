```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
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
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        elif l[i] > l[i + 1]:
            increasing = False
    
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 2, 1]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # False
```

This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. It iterates over the list and checks if each element is greater than or less than the next one. If it finds an element that is not monotonically increasing or decreasing, it sets the corresponding flag to `False`. Finally, it returns `True` if either of the flags is still `True`.