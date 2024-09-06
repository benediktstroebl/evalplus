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

This function calculates the sum of numbers using a formula for the sum of the first n natural numbers, `(1 + 2 + ... + n) = n*(n+1)/2`. This formula is highly efficient and allows the calculation of the sum for any given value of `n`. The code includes a test block to validate the correctness of the function against predefined values.

The function docstring provides clear documentation for the function, including a description of what the function does, what arguments it accepts, and what value it returns. This makes it easy for future users of this function to understand its usage and purpose.