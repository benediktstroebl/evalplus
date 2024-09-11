```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): The input list of numbers.

    Returns:
    list: The input list with each element incremented by 1.

    Example:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This Python script defines a function `incr_list` that takes a list of numbers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to achieve this. The script also includes two test cases to demonstrate the function's behavior.