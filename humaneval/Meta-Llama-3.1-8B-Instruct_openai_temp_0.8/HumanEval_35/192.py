```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

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
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we use Python's built-in `max` function to find the maximum element in a list. The `max` function takes an iterable (like a list or tuple) as an argument and returns the maximum item in that iterable. We also include a docstring to document the function's purpose, parameters, return values, and provide examples of how to use the function.