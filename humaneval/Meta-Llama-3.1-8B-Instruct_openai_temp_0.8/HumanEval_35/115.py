```python
def max_element(lst: list) -> int:
    """Return the maximum element in the list.
    
    Args:
        lst (list): The input list.
    
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

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError: List is empty
```