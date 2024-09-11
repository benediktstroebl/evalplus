```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < t for num in l)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
print(below_threshold([1, 2, 3, 4], 5))     # Expected output: True
print(below_threshold([], 100))             # Expected output: True (empty list is considered below threshold)
```

This script defines the `below_threshold` function, which uses the built-in `all` function and a generator expression to check if all numbers in the list `l` are below the threshold `t`. The test cases demonstrate the function's behavior with different inputs.