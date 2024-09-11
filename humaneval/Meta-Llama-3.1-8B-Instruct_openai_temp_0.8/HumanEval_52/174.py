```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function uses the `all()` function to check if all elements in the input list are below the specified threshold. The `all()` function returns `True` if all elements of the iterable are true. In this case, the iterable is a generator expression that checks each element `i` in the list `lst` against the threshold value. If any element is not below the threshold, the `all()` function will return `False`.