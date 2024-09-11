```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): The list to check.
    
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
    
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        elif l[i] < l[i - 1]:
            increasing = False
    
    return increasing or decreasing


# Test the function
print(monotonic([1, 2, 4, 20])) # Expected: True
print(monotonic([1, 20, 4, 10])) # Expected: False
print(monotonic([4, 1, 0, -10])) # Expected: True
```
In this script, we iterate through the list, checking if we're in an increasing or decreasing sequence. If we ever find an element that doesn't fit the pattern, we set the corresponding flag to `False`. Finally, we return `True` if we're in either an increasing or decreasing sequence, and `False` otherwise.