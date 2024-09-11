```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list numbers are below threshold.
    
    Parameters:
    numbers (list): A list of numbers
    threshold (int): The threshold value
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise
    """
    # Use the built-in all() function with a generator expression to check if all numbers are below the threshold
    return all(num < threshold for num in numbers)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses a generator expression with the `all()` function to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold and `False` otherwise. The script also includes test cases to demonstrate the function's behavior.