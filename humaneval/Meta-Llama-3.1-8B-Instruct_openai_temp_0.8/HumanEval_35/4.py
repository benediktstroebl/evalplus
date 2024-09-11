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
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

**Explanation:**

*   We import no modules as this function can be solved with built-in Python functions.
*   The function `max_element(l: list)` takes a list `l` as an argument and returns its maximum element.
*   Inside the function, we use the built-in `max()` function in Python, which returns the largest item in an iterable or the largest of two or more arguments.
*   We then test the function with the provided examples to ensure it works correctly.