```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the upper limit of a range of numbers. The function leverages the `range` function to generate a sequence of numbers from 1 to `n`, and then uses the `sum` function to add up all the numbers in this sequence, providing the sum of integers from 1 to `n`. The function encapsulates this computation within a straightforward one-liner, eliminating the need for an explicit loop, thereby optimizing efficiency and code simplicity.

This function is designed to be invoked with different values for `n` and it returns an integer representing the sum of the first `n` positive integers, providing a convenient way to calculate this sum for various values of `n`.