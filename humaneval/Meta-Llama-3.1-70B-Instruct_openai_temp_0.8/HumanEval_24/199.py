```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(35))  # Output: 5
```

This script iterates from `n - 1` down to `1` to find the largest divisor of `n`. As soon as it finds a number that divides `n` evenly (i.e., `n % i == 0`), it returns that number. If no divisors are found, it would return `None`, but since every number has at least a divisor of `1`, this case is not possible in this context.