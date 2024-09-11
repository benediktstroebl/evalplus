```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

# Test the function
print(monotonic([1, 2, 4, 20]))  # Should return True
print(monotonic([1, 20, 4, 10]))  # Should return False
print(monotonic([4, 1, 0, -10]))  # Should return True
```

This script defines a function `monotonic` that checks if a list is monotonically increasing or decreasing. It uses the `all` function with generator expressions to check if all pairs of consecutive elements in the list are either all increasing or all decreasing. The `zip` function is used to pair up consecutive elements in the list.