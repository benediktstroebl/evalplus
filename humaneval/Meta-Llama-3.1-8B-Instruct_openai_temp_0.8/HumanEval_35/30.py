```python
def max_element(lst: list) -> int:
    """Return the maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List cannot be empty")
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list of numbers as input and returns the maximum element in the list. It uses Python's built-in `max` function to find the maximum element. It also includes a check to ensure the list is not empty and raises a `ValueError` if it is. The script includes docstrings and example usage to demonstrate how to use the function.