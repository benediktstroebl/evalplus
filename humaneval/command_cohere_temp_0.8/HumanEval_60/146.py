```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Testing the function with different inputs
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n`, which calculates the sum of the first `n` integers using the formula for the sum of the first `n` natural numbers. The function is then tested with different input values, and the expected outputs are printed as comments. Feel free to modify the test values or add more tests to ensure the function behaves as expected. Let me know if you need more information or if you'd like to tackle a new coding problem!