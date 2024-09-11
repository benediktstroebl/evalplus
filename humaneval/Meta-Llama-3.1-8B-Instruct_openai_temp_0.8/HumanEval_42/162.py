### Incrementing List Elements

Here is a self-contained Python script that uses a list comprehension to increment each element in the list by 1.

```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list to be incremented.

    Returns:
        list: The input list with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list with each element incremented by 1. The list comprehension `x + 1 for x in l` is used to achieve this. The function includes a docstring with example usage and a clear description of its behavior.