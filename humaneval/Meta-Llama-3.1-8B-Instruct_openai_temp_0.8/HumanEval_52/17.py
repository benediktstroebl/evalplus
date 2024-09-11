```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.

    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold to check against.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold as input. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, it returns `True`; otherwise, it returns `False`. The example usage demonstrates how to call this function with different inputs.