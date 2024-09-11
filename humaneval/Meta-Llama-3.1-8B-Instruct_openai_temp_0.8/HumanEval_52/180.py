```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

In this script, the `below_threshold` function uses the built-in `all()` function along with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. If any element is false, it returns `False`.