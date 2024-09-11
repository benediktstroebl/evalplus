```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
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
    if not lst:
        raise ValueError("List is empty")
    return max(lst)
```

You can run this script in your Python environment to test the `max_element` function.

Note: The `max` function in Python returns the largest item in an iterable or the largest of two or more arguments. It is a built-in function in Python, so this implementation is concise but may be less efficient than a custom implementation for very large lists.