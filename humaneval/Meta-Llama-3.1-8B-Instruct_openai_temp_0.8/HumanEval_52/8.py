```python
def below_threshold(lst: list, threshold: int):
    """Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers
        threshold (int): The threshold value
    
    Returns:
        bool: True if all numbers are below the threshold, False otherwise
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` which takes a list of numbers and a threshold value as input. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The test cases are included at the end to demonstrate the function's usage.