```python
def below_threshold(l: list, t: int) -> bool:
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
    return all(i < t for i in l)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))  # Expected output: False
```

This script defines a function `below_threshold` that takes a list `l` and a threshold `t` as input, and returns `True` if all numbers in `l` are below `t`, and `False` otherwise. The function uses the `all` function with a generator expression to check this condition. The script then tests the function with the provided examples.