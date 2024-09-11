```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(48))  # Output: 24
```

This script defines the `largest_divisor` function that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates over the numbers from `n-1` down to `1`, and returns the first number for which `n` is divisible evenly.

Note that for prime numbers, the largest divisor is always `1`, as they have no other divisors except for `1` and themselves.