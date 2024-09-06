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

This script defines a function called `sum_to_n`, which takes in an integer `n` as an argument and returns the sum of the first `n` integers. The function uses a mathematical formula to calculate the sum of the first n natural numbers (1 + 2 + ... + n), which is given by `n * (n + 1) // 2`.

The code then includes some tests to validate the function's behavior. It asserts that `sum_to_n(30)` returns 465, `sum_to_n(100)` returns 5050, `sum_to_n(5)` returns 15, `sum_to_n(10)` returns 55, and `sum_to_n(1)` returns 1.

Thus, this Python script solves the problem in a self-contained manner, and the function behavior is explained by the comments within.  If you have any more queries or problems to be solved, please let me know!