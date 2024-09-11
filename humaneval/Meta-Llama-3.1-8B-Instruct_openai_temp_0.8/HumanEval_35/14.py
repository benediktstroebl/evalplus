```python
def max_element(l: list) -> int:
    """
    Return the maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

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

This Python script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. The `max` function is used to find the maximum element, which is a built-in Python function for finding the maximum value in an iterable. The script includes docstrings to provide documentation for the function and test cases to verify its correctness.