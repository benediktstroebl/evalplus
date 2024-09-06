```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes an integer `n` as input and returns the sum of integers from 1 to `n`. Inside the function, it uses the `sum` function along with the `range` function to generate a series of numbers from 1 to `n`, and adds them together to provide the total sum. The `range` function generates numbers incrementally up to `n` (exclusive), ensuring the sequence includes both start and stop values. 

The function effectively calculates the sum of the integers in this range and returns the result, achieving the goal of summing numbers from 1 to a given value of `n`.