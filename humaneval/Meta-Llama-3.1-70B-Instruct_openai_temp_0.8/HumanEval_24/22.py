```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number for which to find the largest divisor

    Returns:
    int: The largest divisor of n, smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(48))  # Output: 24
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input, then iterates from `n-1` down to `1` to find the largest number that divides `n` evenly. It returns the first number it finds that satisfies this condition.

Note that for prime numbers (like 17 in the example), the largest divisor smaller than `n` will always be `1`, since prime numbers only have two distinct divisors: `1` and themselves.