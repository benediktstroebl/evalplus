```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
    l (list): A list of elements

    Returns:
    The maximum element in the list

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list as input and returns its maximum element. The `max` function in Python is used to find the maximum element in the list. The script also includes docstrings to explain the purpose of the function and its usage. Two test cases are included to demonstrate the function's behavior.