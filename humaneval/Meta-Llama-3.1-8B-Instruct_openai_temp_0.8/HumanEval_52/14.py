```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of numbers.
    threshold (int): The maximum allowed value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    
    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in numbers)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in the list are below the specified threshold. It uses the built-in `all` function along with a generator expression to make this check. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If any element is false, `all` returns `False`. The generator expression checks if each number in the list is less than the threshold.

The script includes docstrings for the function and provides two test cases to demonstrate its usage.