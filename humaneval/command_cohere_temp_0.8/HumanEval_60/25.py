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

This function definition and test suite meet the problem requirements: summing the first `n` integers and demonstrating that behavior for a variety of input values. 
The formula `(n * (n + 1)) / 2` is a well-known method for calculating the sum of the first `n` natural numbers, and is used here to provide an efficient solution.

If you would like to see more tests, or have other tests that you want to add to this function, feel free to do so. Adding test cases is always a good way to ensure that your function stays accurate and correct, and it helps to prevent regression when you make changes later. Let me know if I can assist you in adding to the test suite, or we can proceed to other topics or problems that you would like to tackle. Possibilities are endless, so let me know how I can help!