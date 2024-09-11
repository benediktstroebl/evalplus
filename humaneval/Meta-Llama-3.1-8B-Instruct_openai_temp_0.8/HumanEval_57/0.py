```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): The input list to be checked.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(x <= y for x, y in zip(l, l[1:]))
    is_decreasing = all(x >= y for x, y in zip(l, l[1:]))
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script uses Python's built-in `all()` function to check if all elements in the list, starting from the second element (since we're comparing it with the previous one), are less than or equal to the previous one (`x <= y`) for a monotonically increasing list, and greater than or equal to the previous one (`x >= y`) for a monotonically decreasing list. The `zip(l, l[1:])` expression is used to pair each element with its next one. If the list is either increasing or decreasing, the `all()` function will return `True` and the function will return `True`. If the list is neither increasing nor decreasing, the `all()` function will return `False` for either `is_increasing` or `is_decreasing` and the function will return `False`.