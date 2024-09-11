```python
def max_element(l: list):
    """
    Return maximum element in the list.

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

# Test cases
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that uses Python's built-in `max` function to find the maximum element in a list. The `max` function takes an iterable as an argument and returns the largest item in the iterable. The script also includes test cases to verify that the function works correctly.