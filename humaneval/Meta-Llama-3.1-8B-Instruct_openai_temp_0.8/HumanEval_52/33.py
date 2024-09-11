```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        lst (list): A list of numbers.
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
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function in combination with a generator expression to check this condition efficiently. The script includes example usage and a docstring to provide documentation for the function.