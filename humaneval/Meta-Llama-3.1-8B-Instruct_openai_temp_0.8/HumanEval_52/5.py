```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    numbers (list): A list of numbers to check.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in numbers)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

This script defines a function called `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function in combination with a generator expression to check the condition for each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates how to use the function with the provided example inputs.