```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of integers
    threshold (int): The threshold value
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise
    """
    return all(num < threshold for num in numbers)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in a list are below a specified threshold. It uses the built-in `all` function in combination with a generator expression to check the condition for each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage demonstrates the function's behavior with the provided test cases.