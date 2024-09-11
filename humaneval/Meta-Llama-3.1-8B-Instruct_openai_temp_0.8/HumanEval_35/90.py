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

In this script, we define a function `max_element` that takes a list of integers as input and returns the maximum element in the list. We use the built-in `max` function in Python to achieve this, which returns the largest item in an iterable or the largest of two or more arguments. 

We also include docstrings to describe the function's behavior, arguments, and return value, as well as examples of how to use the function. Finally, we test the function with two example inputs to demonstrate its correctness.