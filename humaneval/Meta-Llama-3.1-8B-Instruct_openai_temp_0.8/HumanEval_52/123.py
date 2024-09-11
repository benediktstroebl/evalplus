```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    
    # Use all() with a generator expression to check if all numbers are below threshold
    return all(num < threshold for num in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function uses `all()` with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If at least one element is false, `all()` returns `False`. The test cases demonstrate the function's behavior with different inputs.