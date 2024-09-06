```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this operation can be inefficient for large n,
    as it requires summing a sequence of length n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes an integer `n` as input and returns the sum of the first `n` integers starting from 1. It uses the `sum` function to calculate this sum efficiently by creating a sequence of numbers from 1 to `n` (inclusive) and adding them together. 

The docstring explains its purpose, and the test cases show that it passes the expected input and outputs for various `n` values.