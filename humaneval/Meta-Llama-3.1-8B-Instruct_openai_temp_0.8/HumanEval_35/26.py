```python
def max_element(l: list) -> int:
    """
    Return maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:  # Check if the list is empty
        raise ValueError("List cannot be empty")
    return max(l)  # Use built-in max() function to find the maximum element

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list as input and returns its maximum element. It uses the built-in `max` function to find the maximum element in the list. The script also includes a check to raise a `ValueError` if the list is empty. The function's behavior is demonstrated with two test cases.