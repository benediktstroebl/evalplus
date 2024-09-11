```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    
    Example:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. If any number in the list is not below the threshold, the `all()` function will return `False`.