```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script defines a function `below_threshold` that checks if all elements in a given list are below a specified threshold. It uses the built-in `all()` function along with a generator expression to check if all elements satisfy the condition. If all elements are below the threshold, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.