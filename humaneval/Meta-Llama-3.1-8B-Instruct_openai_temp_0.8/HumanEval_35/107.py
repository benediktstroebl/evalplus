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
    return max(l)

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we use the built-in `max` function to find the maximum element in the list. This function iterates over the list and returns the largest item. The `max_element` function takes a list as input and returns its maximum element. The `-> int` syntax after the argument list indicates that the function returns an integer. The docstring provides a description of the function, its arguments, its return value, and some examples of how to use it.