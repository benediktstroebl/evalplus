```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: Whether all numbers in the list are below threshold.
    
    Example:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all elements in a given list are below a certain threshold. It uses the built-in `all` function with a generator expression to iterate over the list and check each number. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes example use cases for the function.