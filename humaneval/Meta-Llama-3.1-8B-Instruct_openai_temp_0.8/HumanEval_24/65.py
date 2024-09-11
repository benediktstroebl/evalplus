### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, finds the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1
```

This script defines a function `largest_divisor(n)` that calculates the largest divisor of a given number `n` by checking each number from `n-1` down to 1 for divisibility. If a divisor is found, it is immediately returned. If no divisors are found, 1 is returned as the largest divisor (every number is divisible by 1).