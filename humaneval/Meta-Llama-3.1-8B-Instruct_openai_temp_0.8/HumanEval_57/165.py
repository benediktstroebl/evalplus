```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))


# Test the function
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # Expected output: True
    print(monotonic([1, 20, 4, 10]))  # Expected output: False
    print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

In this script, the `monotonic` function uses the `all` function with generator expressions to check two conditions: whether the list is monotonically increasing (`x <= y`) or decreasing (`x >= y`). The `zip` function is used to pair each element with its next one in the list.