```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        The maximum element in the list.

    Example:
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

This script defines a function `max_element` that takes a list of numbers as input and returns the maximum element in the list. It uses Python's built-in `max` function to find the maximum element, which is an efficient and concise way to solve this problem. The script also includes example use cases to demonstrate how to use the function. 

Note that I've added type hints for the `lst` parameter to make it clear that it's a list of numbers, as well as a docstring to provide documentation for the function. I've also included example test cases to demonstrate the function's behavior.