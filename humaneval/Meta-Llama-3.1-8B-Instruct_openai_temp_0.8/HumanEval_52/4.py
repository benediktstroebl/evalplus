```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of integers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < t for num in l)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
print(below_threshold([1, 20, 4, 10], 5))   # Should print: False
```

This script defines the `below_threshold` function, which uses the built-in `all` function and a generator expression to check if all numbers in the input list `l` are below the threshold `t`. If all numbers are below the threshold, `all` returns True; otherwise, it returns False. The script also includes test cases to demonstrate the function's behavior.