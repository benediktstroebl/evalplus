```python
def max_element(lst: list) -> any:
    """Return maximum element in the list.
    
    Args:
    lst: A list of elements of any type.
    
    Returns:
    The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("Cannot find maximum of empty list")
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError
```

This script defines a function `max_element` that takes a list as input and returns the maximum element. It uses the built-in `max` function to find the maximum element. The `max` function returns the largest item in an iterable or the largest of two or more arguments.

However, if the list is empty, the `max` function will raise a `ValueError`. To handle this, we add a check at the beginning of the function and raise a `ValueError` ourselves if the list is empty.

In the example usage section, we demonstrate how to use the function with different lists. We also show that an empty list raises a `ValueError`.