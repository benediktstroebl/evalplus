```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Use the built-in all() function in combination with a generator expression
    # to check if all numbers in the list are below the threshold
    return all(num < threshold for num in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines the `below_threshold` function, which checks if all numbers in the input list are below the specified threshold. It uses the `all()` function in combination with a generator expression to achieve this. The `all()` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If at least one element is false, `all()` returns `False`. The example usage demonstrates how to call the function with different input lists and thresholds.