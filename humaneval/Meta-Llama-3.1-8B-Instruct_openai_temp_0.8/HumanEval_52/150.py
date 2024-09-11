```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.

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
    
    # Check if all numbers in the list are below the threshold
    return all(i < t for i in l)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines the `below_threshold` function, which checks if all numbers in the input list are below the specified threshold. It uses the built-in `all` function with a generator expression to check this condition. The function returns `True` if all numbers are below the threshold and `False` otherwise. The script also includes example use cases to demonstrate the function's behavior.