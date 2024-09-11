```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.

    Args:
        lst (list): A list of integers.
        threshold (int): The upper limit.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

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
print(below_threshold([1, 2, 3, 4], 5))     # False
print(below_threshold([1, 2, 3, 4], 10))    # True
```

This Python script defines a function `below_threshold` that checks if all numbers in a given list are below a certain threshold. The function uses the built-in `all` function in combination with a generator expression to check the condition for each number in the list. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. Otherwise, it returns `False`.