```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))


# Example usage
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if its elements are either monotonically increasing or decreasing. It uses the `all` function in combination with generator expressions to check the monotonicity of the list. The `zip` function is used to pair each element with its successor, and the comparison of these pairs determines whether the list is monotonically increasing or decreasing.