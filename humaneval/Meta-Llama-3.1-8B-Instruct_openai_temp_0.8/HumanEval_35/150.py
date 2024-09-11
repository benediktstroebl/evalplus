### Max Element in List
#### Python Script

```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): List of elements.

    Returns:
        int or float: Maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This script defines a function `max_element` that takes a list as input and returns its maximum element using Python's built-in `max` function. The function includes a docstring that describes its purpose, arguments, return value, and provides examples of its usage. Two test cases are included at the end to demonstrate the function's behavior.