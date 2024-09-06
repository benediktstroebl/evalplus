```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This code defines a function called `sum_to_n` that takes an integer `n` as input and returns the sum of the first `n` integers. It uses the `sum` function to calculate the sum of the range from 1 to `n` (inclusive) using the `range` function. The `range` function generates a sequence of numbers starting from 1 up to `n`, and by using it in the `sum` function, it gets iterated over these numbers and adds them up. 

The function's behavior is demonstrated through pseudo-code like examples in the docstring. It shows that given different input values, the function returns the expected sums.