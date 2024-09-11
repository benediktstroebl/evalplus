```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        int: The maximum element in the list.
    
    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")
    
    # Use the built-in max function to find the maximum element
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```