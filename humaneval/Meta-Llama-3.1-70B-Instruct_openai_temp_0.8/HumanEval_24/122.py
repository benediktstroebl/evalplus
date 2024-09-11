```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(24))  # Expected output: 12
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates over numbers from `n - 1` down to 2 and checks if `n` is divisible by the current number. If it is, the function returns that number. If no divisors are found, it returns 1. The script also includes some test cases to demonstrate its usage.