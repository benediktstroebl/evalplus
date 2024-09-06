```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

This function uses the sum formula for the first n natural numbers, which is given by `n * (n + 1) // 2`. This formula minimizes the number of additions required to compute the sum, making it efficient. The test cases ensure that the function correctly calculates the sum for various values of `n`.  This problem can be solved using different approaches, but this script demonstrates a straightforward and optimized way to accomplish it.

As a language model, I am incapable of running the script internally. However, you can execute it externally and examine if the outcomes align with the expected results. You may also further analyze the function by considering edge cases, expanding the test suite, or researching alternative method to solve the issue. Please feel free to ask any questions or seek additional assistance.