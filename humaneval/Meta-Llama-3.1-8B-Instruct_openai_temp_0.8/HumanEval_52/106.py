```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of integers `lst` and an integer `threshold` as input. It uses the built-in `all` function along with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to demonstrate the function's correctness.