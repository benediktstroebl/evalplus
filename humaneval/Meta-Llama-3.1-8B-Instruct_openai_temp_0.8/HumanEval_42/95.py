```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: The input list with each element incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

To test this function, you can run the script with the following lines:

```python
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to create a new list where each element is the input element incremented by 1. This is a concise and efficient way to perform the operation.