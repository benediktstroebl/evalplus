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
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. The `max` function in Python is used to find the maximum element in a list. The script also includes docstrings to provide documentation for the function and examples of how to use it. The function is then tested by calling it with two different lists and printing the results.