```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
print(max_element([]))  # Expected output: raises ValueError
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. If the list is empty, it raises a `ValueError`. The function uses the built-in `max` function to find the maximum element, which makes the code concise and efficient. The test cases at the end demonstrate the function's usage and behavior.