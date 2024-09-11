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
    
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))   # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
This script defines a function `monotonic` that takes a list of numbers as input and returns `True` if the elements are monotonically increasing or decreasing, and `False` otherwise. It then includes test cases to demonstrate the function's behavior.