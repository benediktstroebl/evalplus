```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return sum(range(1, n + 1))
```
This Python script defines a function `sum_to_n` that calculates the sum of integers from 1 to `n` (`n` is an integer input to the function). It uses the `range` function to generate a series of numbers from 1 to `n` and leverages the `sum` function to add these numbers together. 

The function returns the sum of the integers as an integer value. 

The optional argument, `return`, indicates that the function will return a value after computation.