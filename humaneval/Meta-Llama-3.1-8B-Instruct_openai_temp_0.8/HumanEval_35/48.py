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
    if not l:
        raise ValueError("List is empty")
    return max(l)

# Test cases
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
print(max_element([]))  # Expected output: ValueError
```