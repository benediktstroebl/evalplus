```python
def incr_list(l: list):
    """Return list with elements incremented by 1.

    Args:
        l (list): Input list of numbers.

    Returns:
        list: List with elements incremented by 1.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list of numbers as input and returns a new list with each element incremented by 1. The function uses a list comprehension to achieve this. The example usage demonstrates how to use the function with two different input lists.