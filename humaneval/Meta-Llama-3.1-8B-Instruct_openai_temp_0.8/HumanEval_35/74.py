```python
def max_element(lst: list):
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of elements.
    
    Returns:
    The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError
```

Note that this script uses the built-in `max()` function to find the maximum element in the list. If the list is empty, it raises a `ValueError` as per the problem statement.