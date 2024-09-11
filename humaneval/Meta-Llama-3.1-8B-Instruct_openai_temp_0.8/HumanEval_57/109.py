```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    is_increasing = all(x <= y for x, y in zip(l, l[1:]))
    is_decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([1, 3, 2, 4]))  # Expected output: False
print(monotonic([10, 10, 10, 10]))  # Expected output: True
```

This script defines a function `monotonic` that checks if the elements of a given list are monotonically increasing or decreasing. It uses the `all` function with generator expressions to check if each element is less than or equal to the next one (for increasing) or greater than or equal to the next one (for decreasing). If either of these conditions is true for all pairs of adjacent elements, the function returns `True`; otherwise, it returns `False`. The script also includes several test cases to demonstrate the function's behavior.