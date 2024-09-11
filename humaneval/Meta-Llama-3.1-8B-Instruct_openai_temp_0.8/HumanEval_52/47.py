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


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected: False
```

This script defines a function `below_threshold` that takes a list of integers `lst` and a threshold value `threshold` as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes the original test cases from your problem statement to demonstrate the function's usage.