```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)


# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))    # Output: False
```

In this script, the `below_threshold` function uses the built-in Python function `all()` in combination with a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If at least one element is false, `all()` returns `False`. The generator expression `num < threshold for num in lst` checks each number in the list against the threshold.