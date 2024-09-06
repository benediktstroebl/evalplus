```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Tests
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function definition along with the docstring and test assertions provide a self-contained unit for the `sum_to_n` function.  The formula n * (n + 1) // 2 is used to calculate the sum of the first n natural numbers.  The assertions help to verify that the function computes the correct sums for various values of n.  The tests use the `assert` statement to check if the output of the `sum_to_n` function is correct for a given input.  If the output is correct, the assert statement passes without errors.  If the output is incorrect, the assert statement raises an error, indicating that the function is incorrect.  This type of testing is fundamental in software development to ensure that functions operate as expected and the results are correct.  It also provides illustrative examples of how to use the `sum_to_n` function correctly.  Overall, this solution is efficient, well-documented, and aligned with coding best practices, making it highly robust and readable.  It is also extensible for more rigorous testing and different input scenarios if needed.  Lastly, the solution provides a reusable function that can be applied to various scenarios requiring the summation of consecutive integers.