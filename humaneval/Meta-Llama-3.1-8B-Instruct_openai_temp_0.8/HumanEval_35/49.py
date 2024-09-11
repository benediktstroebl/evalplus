### Maximum Element in a List
Here's a Python function to find the maximum element in a list:

```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): Input list of numbers.
    
    Returns:
    int: Maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:  # Handle empty list
        raise ValueError("List cannot be empty")
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This code defines a function `max_element` that takes a list as input, checks if the list is empty, and returns the maximum element using the built-in `max` function. The function includes a docstring that describes its behavior, arguments, return value, and provides examples of usage.