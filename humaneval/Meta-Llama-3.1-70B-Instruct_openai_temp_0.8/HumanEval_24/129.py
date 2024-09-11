```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest divisor of n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(24))  # Expected output: 12
print(largest_divisor(17))  # Expected output: 1
```

This script defines the `largest_divisor` function, which iterates over all numbers smaller than `n` in descending order and returns the first number that divides `n` evenly (i.e., with no remainder). The script also includes test cases to demonstrate the function's usage.