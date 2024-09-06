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
This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the number of integers to sum. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of the first `n` integers. The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the numbers in this sequence. The result is then returned as the output of the function. 

The function includes a docstring comprising a description of its purpose, information about its arguments, and the return type. This documentation is useful for understanding the function and its usage.

The given tests are constructed to examine various scenarios of the `sum_to_n` function's behavior. They pass multiple test cases with the expected output, confirming the function's correctness and stability against different input scenarios.