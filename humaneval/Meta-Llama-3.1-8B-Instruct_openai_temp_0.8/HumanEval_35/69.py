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

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function called `max_element` that takes a list `l` as input and returns the maximum element from that list. The `max` function is a built-in Python function that returns the largest item in an iterable or the largest of two or more arguments.