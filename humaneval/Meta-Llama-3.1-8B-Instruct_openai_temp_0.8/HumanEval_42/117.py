```python
def incr_list(numbers: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers where each element is incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [n + 1 for n in numbers]
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list with each element incremented by 1. The function uses a list comprehension to achieve this in a concise and efficient way.

You can test the function using the provided examples or by creating your own test cases. For example:

```python
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
print(incr_list([-1, 0, 1]))  # Output: [0, 1, 2]
print(incr_list([10, 20, 30]))  # Output: [11, 21, 31]
```