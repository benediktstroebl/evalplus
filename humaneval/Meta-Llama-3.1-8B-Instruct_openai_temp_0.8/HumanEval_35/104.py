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

In this script, we use the built-in `max()` function in Python, which returns the largest item in an iterable (like a list or tuple). If the list is empty, it raises a `ValueError`. If you want to handle this case, you could add a check at the beginning of your function:

```python
def max_element(l: list):
    if not l:
        return None  # or you could raise a ValueError or handle it in any other way
    return max(l)
```