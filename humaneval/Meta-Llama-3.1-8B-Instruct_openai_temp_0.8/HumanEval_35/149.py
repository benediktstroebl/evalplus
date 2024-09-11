### Max Element in List
```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        int: The maximum element in the list.
    
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
This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses the built-in `max` function in Python to find the maximum element.

Note that the `max` function works with lists of any type that supports the comparison operator, not just integers. If you want to work with a more general type (e.g., floats or complex numbers), the `max` function will still work correctly.