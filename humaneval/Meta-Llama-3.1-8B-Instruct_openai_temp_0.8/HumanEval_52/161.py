```python
def below_threshold(lst: list, threshold: int):
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    
    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This Python script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. It uses the built-in `all` function in combination with a generator expression to efficiently check each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`.