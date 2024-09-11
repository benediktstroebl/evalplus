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

This script defines the `below_threshold` function, which uses the built-in `all` function with a generator expression to check if all numbers in the list are below the given threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage section demonstrates how to use this function with the provided test cases.