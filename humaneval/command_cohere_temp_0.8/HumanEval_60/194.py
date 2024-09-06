```python
def sum_to_n(n):
    """Returns the sum of the first n numbers (1 through n)."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, representing a target number. The function calculates and returns the sum of the first 'n' numbers, ranging from 1 to n. It achieves this by utilizing the `sum` function in combination with `range`, which generates a sequence of numbers from 1 to 'n' (inclusive). This sequence is then summed, resulting in the total of the first 'n' numbers.