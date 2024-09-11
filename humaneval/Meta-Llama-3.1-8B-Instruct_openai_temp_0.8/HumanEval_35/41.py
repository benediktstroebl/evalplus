```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)


# Test the function
print(max_element([1, 2, 3]))  # Should print: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Should print: 123
print(max_element([]))  # Should raise ValueError: List is empty
```
This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It includes example use cases and tests for edge cases, such as an empty list.