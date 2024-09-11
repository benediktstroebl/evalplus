```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of numbers to check.
    threshold (int): The maximum allowed value.

    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function uses the `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements in the iterable are true, and `False` otherwise. If at least one number is not below the threshold, `all()` will return `False`.