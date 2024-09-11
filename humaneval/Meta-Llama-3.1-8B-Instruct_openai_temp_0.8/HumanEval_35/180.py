```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The maximum number in the list.

    Example:
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


# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of numbers as input and returns the maximum number. It checks if the list is empty and raises a `ValueError` if it is. The `max` function is used to find the maximum element in the list, which is then returned. The function is tested with two examples.