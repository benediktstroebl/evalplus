```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of elements to be incremented.

    Returns:
        list: List with elements incremented by 1.
    """
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list as input, increments each element by 1 using a list comprehension, and returns the resulting list. The test cases at the end demonstrate the function's behavior.