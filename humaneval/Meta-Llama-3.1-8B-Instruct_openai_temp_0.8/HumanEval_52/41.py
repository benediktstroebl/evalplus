```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: Whether all numbers in the list are below the threshold.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < t for num in l)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))    # False
```

This script defines a function `below_threshold` that checks whether all numbers in the input list `l` are below the given threshold `t`. The function uses the built-in `all` function in combination with a generator expression to achieve this. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. The generator expression generates boolean values indicating whether each number in the list is less than the threshold.