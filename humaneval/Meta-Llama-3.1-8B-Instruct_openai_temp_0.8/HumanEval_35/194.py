```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
    l (list): A list of elements.

    Returns:
    The maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

Alternatively, you could implement the `max_element` function without using the built-in `max` function for educational purposes:
```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
    l (list): A list of elements.

    Returns:
    The maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_val = l[0]
    for element in l:
        if element > max_val:
            max_val = element
    return max_val

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```