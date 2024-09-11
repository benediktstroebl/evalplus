```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if list is empty
    if len(l) == 0:
        return True
    
    # Initialize flag to indicate increasing or decreasing
    increasing = decreasing = True
    
    # Iterate through list from start to second last element
    for i in range(len(l) - 1):
        # If elements are not increasing
        if l[i] > l[i + 1]:
            increasing = False
        # If elements are not decreasing
        elif l[i] < l[i + 1]:
            decreasing = False
    
    # Return True if list is increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([3, 3, 4, 4]))    # True
```