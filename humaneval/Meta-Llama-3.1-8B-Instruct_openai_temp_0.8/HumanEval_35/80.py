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
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

In this code:

1.  We define a function `max_element` that takes a list `lst` as input.
2.  We use the built-in `max` function to find the maximum element in the list.
3.  We add a docstring to provide documentation for the function, including a description, arguments, return value, and examples.
4.  We test the function with two examples to demonstrate its usage.