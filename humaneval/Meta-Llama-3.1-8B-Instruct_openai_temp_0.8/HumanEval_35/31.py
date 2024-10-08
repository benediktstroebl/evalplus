### Python Script to Find Maximum Element in a List
```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.
    
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
    return max(lst)


# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```
This script defines a function `max_element` that takes a list as input and returns the maximum element using the built-in `max` function in Python. The function is tested with two example lists, and the results are printed to the console.