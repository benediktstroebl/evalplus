```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Check if the list is empty
    if not lst:
        raise ValueError("List is empty")
    
    # Use built-in max function to find the maximum element in the list
    return max(lst)


# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This Python script includes a function called `max_element` that takes a list of integers as an argument and returns the maximum element in the list. If the list is empty, it raises a `ValueError`. The function uses the built-in `max` function to find the maximum element in the list, which is a more concise and efficient way to do it. The script also includes example usage to demonstrate how to use the `max_element` function.