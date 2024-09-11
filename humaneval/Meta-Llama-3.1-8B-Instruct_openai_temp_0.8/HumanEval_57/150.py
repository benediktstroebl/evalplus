```python
def monotonic(l: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if list is monotonically increasing
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    
    # Check if list is monotonically decreasing
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    # Return True if list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. The function uses list comprehension with the `all` function to check if the elements in the list are in non-decreasing or non-increasing order. The function returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The script includes test cases to demonstrate the function's behavior.