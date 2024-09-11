```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.

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
    # Check if list is empty
    if len(l) < 2:
        return True
    
    increasing = decreasing = True
    
    # Check if list is increasing or decreasing
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        elif l[i] > l[i-1]:
            decreasing = False
    
    # Return True if list is increasing or decreasing, False otherwise
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 5, 5, 5]))  # True
print(monotonic([]))  # True
print(monotonic([1]))  # True
```