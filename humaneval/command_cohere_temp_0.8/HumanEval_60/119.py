```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers (1 + 2 + ... + n)

# Testing the function with different input values
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n`, which calculates the sum of the first `n` integers using the formula for the sum of the first `n` natural numbers. The function is then tested with different input values, ensuring that it produces the expected outputs based on the formula.

The `sum_to_n` function is straightforward and optimized for calculating the sum of integers up to `n`. It avoids the iterative process involved in a straightforward implementation, which could lead to performance issues for large `n`. Instead, it leverages the mathematical sum formula to calculate the result directly, making it more efficient for large input values.

The tests confirm that the function behaves as expected, returning the correct sum for various values of `n`. This comprehensive testing approach ensures that the function handles different cases accurately and conforms to the specified requirement, reinforcing its reliability.  This well-designed solution adheres to Python best practices and is optimized for both accuracy and efficiency.