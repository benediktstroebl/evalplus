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
    # Check if the list is decreasing
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    
    # Check if the list is increasing
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    
    # Return True if the list is either increasing or decreasing
    return is_decreasing or is_increasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This Python script defines a function `monotonic(l)` that checks if a list of numbers is either monotonically increasing or decreasing. It uses the `all()` function in combination with a generator expression to check for both increasing and decreasing sequences. The function returns `True` if the list is either increasing or decreasing, and `False` otherwise. The script includes example use cases to demonstrate the function's behavior.