```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List cannot be empty")
    return max(lst)

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element. If the list is empty, it raises a `ValueError` because the maximum element cannot be found in an empty list. The example usage demonstrates how to use the function.