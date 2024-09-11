```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List cannot be empty")
    return max(lst)  # Return the maximum element in the list

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we've implemented a function called `max_element` that takes a list of integers as input and returns the maximum element in the list. The function checks if the list is empty and raises a `ValueError` if it is. Otherwise, it uses the built-in `max` function to find the maximum element in the list and returns it. The script includes example usage to demonstrate how to use the `max_element` function.