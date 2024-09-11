```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

This script defines a function `largest_divisor(n)` that finds the largest number smaller than `n` that divides `n` evenly. The function iterates from `n-1` down to `1`, checking each number to see if it's a divisor of `n`. As soon as it finds one, it returns that number. If no divisors are found (which shouldn't happen for any positive `n`), the function will return `0`, but since we're checking from `n-1` down, we're guaranteed to find at least one divisor, so this case will never occur.