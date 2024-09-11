```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Should return True
print(below_threshold([1, 20, 4, 10], 5))   # Should return False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as arguments. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.