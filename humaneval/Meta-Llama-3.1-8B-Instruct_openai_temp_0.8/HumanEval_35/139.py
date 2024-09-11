```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. The function uses the built-in `max` function to find the maximum element. It also includes error handling to raise a `ValueError` if the input list is empty. The script includes example use cases and prints the results to demonstrate the function's behavior.