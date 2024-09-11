```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The maximum allowed value.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    
    # Use the built-in all() function to check if all elements in the list are below the threshold
    # Use a generator expression to iterate over the list and check each element
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all elements in a given list are below a specified threshold. It uses the `all()` function, which returns `True` if all elements of an iterable (in this case, a generator expression) are true. If any element is false, `all()` returns `False`. This approach is concise and efficient.