```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (since 1 divides every number evenly)
```

In this script, we define a function `largest_divisor(n)` that iterates over numbers from `n-1` down to 1. When it finds a number `i` that divides `n` evenly (i.e., `n % i == 0`), it returns this `i`. This is the largest number smaller than `n` that divides `n` evenly.