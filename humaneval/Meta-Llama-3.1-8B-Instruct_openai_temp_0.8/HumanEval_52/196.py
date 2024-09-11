```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses the built-in `all` function with a generator expression to check whether all numbers in the list are below the threshold. If the generator expression returns `True` for all numbers, the `all` function returns `True`; otherwise, it returns `False`.