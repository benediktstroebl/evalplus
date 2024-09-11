```python
def max_element(lst: list):
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        The maximum element in the list.
    
    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))   # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
try:
    print(max_element([]))  # This should raise a ValueError
except ValueError as e:
    print(e)  # Output: List is empty
```

This script defines a function `max_element` that takes a list as input and returns its maximum element. If the list is empty, it raises a `ValueError`. The script also includes example use cases to demonstrate how to use the function.