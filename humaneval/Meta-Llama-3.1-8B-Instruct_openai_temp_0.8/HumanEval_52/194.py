```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the function `below_threshold` uses the built-in Python function `all()` in combination with a generator expression to check if all numbers in the list are below the threshold. If all numbers meet this condition, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate its functionality.