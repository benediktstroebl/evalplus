```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the range to be summed.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the formula for the sum of an arithmetic series to calculate the result in constant time, making it more efficient than a naive loop-based approach for large values of `n`. The test cases at the end demonstrate the function's correctness.