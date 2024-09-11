```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
        l (list): A list of numbers.
        t (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    
    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(i < t for i in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function with a generator expression to check the condition. The script includes docstrings and test cases to demonstrate the function's usage.