```python
def max_element(l: list):
    """Return maximum element in the list.
    
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
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")
    
    # Initialize max_element with the first element of the list
    max_element = l[0]
    
    # Iterate over the rest of the list to find the maximum element
    for element in l[1:]:
        # If the current element is greater than max_element, update max_element
        if element > max_element:
            max_element = element
    
    # Return the maximum element
    return max_element

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list. It first checks if the list is empty, and raises a `ValueError` if it is. Then, it initializes `max_element` with the first element of the list, and iterates over the rest of the list to find the maximum element. If a larger element is found, `max_element` is updated. Finally, the maximum element is returned.

The script also includes example usage of the `max_element` function, which demonstrates its functionality.