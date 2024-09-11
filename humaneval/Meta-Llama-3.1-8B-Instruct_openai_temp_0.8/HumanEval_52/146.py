```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that takes a list of integers and a threshold value as arguments. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. If at least one element is false, `all` returns `False`. The function returns a boolean value indicating whether all numbers in the list are below the threshold.