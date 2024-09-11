```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    # Use all() function to check if all elements in the list are below threshold
    # The all() function returns True if all elements of the iterable are true
    return all(num < threshold for num in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

This Python script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the `all()` function in combination with a generator expression to achieve this. The script also includes test cases to verify the function's correctness.