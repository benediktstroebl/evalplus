```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): A list of numbers.

    Returns:
        The maximum number in the list.

    Example:
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

This script defines a function `max_element` that takes a list `l` as input and returns its maximum element. It uses Python's built-in `max` function to find the maximum element in the list. The example usage at the end demonstrates how to use the `max_element` function with different lists.