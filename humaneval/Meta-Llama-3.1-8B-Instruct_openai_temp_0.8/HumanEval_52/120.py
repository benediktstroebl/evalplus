```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(i < threshold for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, the `below_threshold` function takes a list of integers and a threshold value as input. It uses the built-in `all` function with a generator expression to check if all numbers in the list are less than the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate the function's usage and output.