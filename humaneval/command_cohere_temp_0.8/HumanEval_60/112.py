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
This Python script defines a function `sum_to_n` that calculates the sum of integers from 1 to `n` (inclusive) and returns the result. The function uses the `sum` function to calculate the sum of the range of numbers provided by `range(1, n + 1)`, which includes both the starting value of 1 and the ending value of `n`. The `range` function generates all the numbers between the two provided endpoints, and including the endpoints themselves. 

The function's comment provides a brief description of its purpose, highlights the argument `n` as the number of integers to sum, and confirms that it returns the sum as an integer.