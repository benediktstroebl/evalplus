```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Testing the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
try:
    print(max_element([]))  # Expected output: ValueError
except ValueError as e:
    print(e)
```

This Python script defines a function called `max_element` which takes a list of integers as input, finds the maximum element in the list, and returns it. If the list is empty, it raises a ValueError. Finally, it tests the function with some examples.