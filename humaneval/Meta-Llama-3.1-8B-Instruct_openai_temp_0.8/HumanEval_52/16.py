```python
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.

    Example:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < t for num in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
print(below_threshold([1, 20, 4, 10], 5))   # Should print: False
```

This script defines a function `below_threshold` that checks if all numbers in a list are below a given threshold. It uses the built-in `all` function with a generator expression to check each number in the list. The test cases at the end demonstrate the function's behavior.