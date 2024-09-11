```python
def max_element(lst: list):
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # check if the list is empty
        raise ValueError("List is empty")
    return max(lst)  # return the maximum element

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, I've made the following improvements:

1. Renamed the function parameter from `l` to `lst` for clarity.
2. Added a check to ensure the list is not empty before attempting to find its maximum element.
3. Used the built-in `max()` function to find the maximum element in the list, which provides a more concise and efficient solution.