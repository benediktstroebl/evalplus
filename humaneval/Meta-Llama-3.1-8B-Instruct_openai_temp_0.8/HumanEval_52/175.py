### below_threshold Function
```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.

    Args:
        numbers (list): A list of numbers to check.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that checks if all numbers in the input list are below the specified threshold. The `all()` function is used with a generator expression to check this condition. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`.