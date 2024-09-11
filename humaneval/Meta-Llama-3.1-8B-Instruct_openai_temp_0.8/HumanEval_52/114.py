```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        numbers (list): A list of numbers to check.
        threshold (int): The threshold value to compare with.
    
    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value, and returns `True` if all numbers in the list are below the threshold. The function uses the built-in `all` function and a generator expression to check each number in the list. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `num < threshold for num in numbers` checks each number in the list against the threshold.