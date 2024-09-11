```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. If any number is not below the threshold, `all()` will return `False`. Otherwise, it returns `True`.