```python
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
    l (list): A list of numbers.
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
```

This script defines a function `below_threshold` that takes a list of numbers `l` and a threshold value `t` as input. It then uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`.