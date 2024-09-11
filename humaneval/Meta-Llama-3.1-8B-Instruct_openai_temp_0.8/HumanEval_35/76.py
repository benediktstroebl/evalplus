```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    The maximum element in the list.
    
    Example:
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

This script defines a function `max_element` that returns the maximum element in a given list. It uses the built-in `max` function to find the maximum element, which is the most efficient way to solve this problem in Python. The function includes a docstring with a description, parameters, return value, and examples to make it easy to use and understand. The script also includes test cases to demonstrate the function's usage.