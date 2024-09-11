```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): Input list of elements.

    Returns:
        The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list `lst` as input and returns the maximum element using the built-in `max` function in Python. The function includes a docstring that describes its purpose, parameters, return value, and example use cases. The script then tests the function with two example lists.