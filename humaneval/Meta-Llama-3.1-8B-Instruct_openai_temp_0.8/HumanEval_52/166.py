```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.

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

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the `all()` function in combination with a generator expression to check this condition. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script includes docstrings to document the function's behavior and provides two test cases to demonstrate its usage.