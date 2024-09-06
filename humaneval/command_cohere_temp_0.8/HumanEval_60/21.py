```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This script defines the `sum_to_n` function, which calculates the sum of the first `n` integers using the formula for the sum of the first `n` natural numbers. The function is then tested with a variety of input values to ensure it returns the expected results.