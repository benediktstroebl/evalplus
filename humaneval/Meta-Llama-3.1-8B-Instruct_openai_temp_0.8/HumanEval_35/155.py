```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is empty
    if not lst:
        raise ValueError("List is empty")

    # Use the built-in max function to find the maximum element
    return max(lst)
```

You can run this script in a Python environment to test the `max_element` function.