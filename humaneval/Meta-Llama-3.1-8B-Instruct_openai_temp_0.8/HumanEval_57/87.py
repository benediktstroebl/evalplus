```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of integers or floats.
    
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
    return (all(x <= y for x, y in zip(l, l[1:])) or 
            all(x >= y for x, y in zip(l, l[1:])))


# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 3, 6, 10, 15]))  # True
print(monotonic([15, 10, 6, 3, 1]))  # True
print(monotonic([1, 3, 7, 5, 2]))  # False
print(monotonic([2, 5, 7, 9, 1]))  # False
```

In this script, we define the `monotonic` function, which checks if the elements in a list are monotonically increasing or decreasing. The function uses the `all` function in combination with a generator expression to check if all consecutive pairs of elements in the list satisfy the condition of being either monotonically increasing or decreasing. If all pairs satisfy the condition, the function returns `True`; otherwise, it returns `False`.