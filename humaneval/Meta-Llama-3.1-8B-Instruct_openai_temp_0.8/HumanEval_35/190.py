```python
def max_element(l: list):
    """
    Return maximum element in the list.
    
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

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

In this script, we define a function `max_element` that takes a list `l` as an argument. The `max` function is used to find the maximum element in the list, and its result is returned. We then test the function with two examples.