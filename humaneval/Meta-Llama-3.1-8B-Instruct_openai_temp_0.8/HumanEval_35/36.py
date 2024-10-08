```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Should print: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Should print: 123
```

This script defines a function `max_element` that takes a list of numbers as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element. The function is then tested with two examples, and the results are printed to the console.