```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Parameters:
    numbers (list): A list of numbers to check.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    return all(n < threshold for n in numbers)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in a list are below a given threshold. The function uses the built-in `all` function with a generator expression to check each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script includes two test cases to demonstrate the function's behavior.