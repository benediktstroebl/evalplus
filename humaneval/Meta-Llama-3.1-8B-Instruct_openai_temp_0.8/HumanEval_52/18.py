```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of integers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(i < t for i in l)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script defines a function `below_threshold` that takes a list `l` and an integer `t` as input. It uses the built-in `all` function with a generator expression to check if all elements in the list are below the threshold. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise. The function returns the result of this check. The script includes docstrings and test cases to demonstrate the function's behavior.