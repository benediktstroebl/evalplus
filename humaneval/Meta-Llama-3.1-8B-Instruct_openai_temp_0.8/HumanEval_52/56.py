```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.

    Args:
        lst (list): A list of numbers.
        threshold (int): The maximum allowed threshold.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script defines a function `below_threshold` that takes a list of numbers and a threshold value as arguments. The function uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold, and `False` otherwise. The script also includes example usage and test cases.