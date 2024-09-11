```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """Return True if all numbers in the list numbers are below threshold threshold.
    
    Args:
        numbers (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    # Use the built-in all() function to check if all elements in the list are below the threshold
    return all(num < threshold for num in numbers)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a certain threshold. The function uses a generator expression to iterate over the list and the built-in `all()` function to check if all elements meet the condition. The script also includes test cases to verify the function's behavior.