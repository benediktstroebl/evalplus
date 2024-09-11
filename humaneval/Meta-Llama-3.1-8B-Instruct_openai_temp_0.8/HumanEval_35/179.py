```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

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
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, I've defined a function `max_element` that takes a list as input and returns its maximum element. This is achieved by using the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The function includes docstrings to provide documentation and examples of usage. 

Note: I changed the variable name `l` to `lst` to follow PEP 8, the official Python style guide. I also changed it to `-> int` in the function docstring to specify the return type of the function.