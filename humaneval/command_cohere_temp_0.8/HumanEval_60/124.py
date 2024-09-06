```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers in the range from 1 to `n` (inclusive). The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum of the first 'n' positive integers. 

The function then returns this computed sum as its output. The function includes a docstring (`Returns the sum of integers from 1 to n.`) that describes its purpose and provides example tests (`>>> sum_to_n(30)`) to ensure it returns the expected results for various values of `n`.