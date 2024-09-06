```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Test suite
def test_sum_to_n():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1

# Run the tests when the script is directly executed
test_sum_to_n()
```

The function `sum_to_n` calculates the sum of numbers from 1 to `n` using the sum formula for the first n natural numbers. The test suite verifies the correctness of the function against predefined values. When executed directly, the script runs the test suite to validate the `sum_to_n` function's correctness. 

**Note:** The formula `n (n + 1) / 2` is a mathematical formula that calculates the sum of the first n natural numbers. This formula is commonly used in computer science and programming to solve this type of problem.