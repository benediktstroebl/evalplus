```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): A threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script implements a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. It uses the built-in `all` function along with a generator expression to check this condition. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are `True`, and `False` otherwise. The test cases demonstrate the function's usage and expected output.