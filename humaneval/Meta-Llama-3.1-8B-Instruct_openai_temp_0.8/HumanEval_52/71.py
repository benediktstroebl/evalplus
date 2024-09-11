```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.

    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in the given list are below the specified threshold. It uses the built-in `all` function with a generator expression to check this condition. The `all` function returns True if all elements of the given iterable (in this case, the generator expression) are True. If any element is False, `all` returns False. The function is then tested with the provided example cases.