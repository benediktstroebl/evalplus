```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The maximum element in the list.

    Raises:
    ValueError: If the list is empty.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Output: Will raise ValueError
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. If the list is empty, it raises a `ValueError`. The function uses the built-in `max` function to find the maximum element in the list. The script also includes test cases to demonstrate the function's behavior.