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
    if not lst:  # check if the list is empty
        raise ValueError("List is empty")
    return max(lst)  # return the maximum element using the built-in max function

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list of integers and returns the maximum element. It checks if the list is empty and raises a `ValueError` if it is. Otherwise, it uses the built-in `max` function to find the maximum element. The function includes docstrings to provide documentation and examples of its usage.