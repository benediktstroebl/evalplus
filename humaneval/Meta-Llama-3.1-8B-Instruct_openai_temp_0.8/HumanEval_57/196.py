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
    # Sort the list and compare it with the original list
    return sorted(l) == l or sorted(l, reverse=True) == l

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

However, note that the function above has a time complexity of O(n log n) due to the sorting operation. A more efficient approach would be to compare each pair of adjacent elements in the list, resulting in a time complexity of O(n):

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
    # Check if the list is empty
    if len(l) < 2:
        return True
    
    increasing = decreasing = True
    
    # Compare each pair of adjacent elements
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    
    # Return True if the list is either increasing or decreasing
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```