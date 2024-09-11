```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    The maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, the `max_element` function takes a list `l` as input and returns the maximum element in the list. It uses Python's built-in `max` function to find the maximum element. The example usage at the end demonstrates how to use the `max_element` function with two different lists.