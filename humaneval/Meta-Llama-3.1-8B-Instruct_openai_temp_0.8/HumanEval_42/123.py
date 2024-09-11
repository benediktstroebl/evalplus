```python
def incr_list(l: list):
    """Return list with elements incremented by 1.
    Args:
        l (list): List of numbers to increment.
    Returns:
        list: List with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3])) # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that uses a list comprehension to increment each element in the input list `l` by 1. The function is then tested with the provided test cases to verify its correctness.