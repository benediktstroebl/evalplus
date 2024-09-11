```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold t.
    
    Args:
        lst (list): A list of numbers to check.
        threshold (int): The maximum allowed value.

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

This script defines a function `below_threshold` that takes a list `lst` and an integer `threshold` as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function in combination with a generator expression to check each number in the list. The script also includes some example test cases to demonstrate the function's behavior.