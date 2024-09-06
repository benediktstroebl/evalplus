```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Note: this operation can be inefficient for large n,
    as it uses a simple loop to generate the sum.
    """
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes an integer `n` as input and returns the sum of the first `n` integers starting from 1. It utilizes the `sum` function to calculate this cumulative sum efficiently. The function includes a docstring with notes on its purpose and behavior, and it handles a variety of test cases.