```python
def max_element(l: list) -> int:
    """
    Return maximum element in the list.

    Args:
    l (list): A list of integers.

    Returns:
    int: The maximum element in the list.

    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)


# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. The `max` function is used to find the maximum element, which is a built-in function in Python. The script then tests the function with two examples to demonstrate its usage.