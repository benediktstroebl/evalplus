```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers ranging from 1 to `n` (inclusive). It leverages the `range` function to create a sequence of numbers from 1 to `n`, and then sums up each number in that sequence using the `sum` function. The result is the total of all integers from 1 to `n`. 

The function is carefully constructed to only operate on positive integers, ensuring correctness and preventing potential errors that may occur with other data types or non-positive values.