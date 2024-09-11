```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
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

This script defines a function `max_element` that takes a list as input and returns its maximum element. It uses the built-in `max` function in Python to find the maximum element. The example usage and docstring provide documentation for the function, and the test at the end verifies that it works as expected.