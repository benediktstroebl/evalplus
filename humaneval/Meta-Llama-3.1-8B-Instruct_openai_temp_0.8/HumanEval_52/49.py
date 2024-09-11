```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    
    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
print(below_threshold([1, 20, 4, 10], 5))   # Should print: False
```

This script defines a function `below_threshold` that takes a list `lst` and a threshold `threshold` as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The function is then tested with two examples.