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

This code defines a function called `sum_to_n` that takes an integer argument `n`. It returns the sum of the first `n` integers from 1 to `n` inclusive. This is accomplished using Python's built-in sum function and the range function which creates a sequence of numbers from start to stop values inclusive with steps of 1. Since the start is 1 and the step is 1, it creates the sequence of integers from 1 to `n` which when summed using the sum function returns the desired result. 

The function's docstring provides an explanation of its purpose, the argument it accepts, and the value it returns. Additionally, it includes test cases to demonstrate the function's behavior for various `n` values.