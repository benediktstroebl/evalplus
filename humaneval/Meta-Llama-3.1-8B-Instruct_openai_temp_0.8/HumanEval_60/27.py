```python
def sum_to_n(n: int):
    """
    Sum numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

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

This script defines the `sum_to_n` function, which uses the mathematical formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The test cases at the end of the script demonstrate the function's behavior.