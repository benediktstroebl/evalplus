```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

Explanation:
The function `below_threshold` uses Python's built-in `all()` function and a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements of the iterable are true. If at least one element is false, `all()` returns `False`. The generator expression `i < threshold for i in lst` generates a sequence of boolean values indicating whether each number in the list is less than the threshold.