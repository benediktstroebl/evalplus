```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.

    Example:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1  # Initialize result as 1
    base = 2  # Define base as 2
    while n > 0:  # Continue loop until n becomes 0
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Update base and n for next iteration
        base = (base * base) % p
        n = n // 2  # Right shift n for next iteration
    return result
```

This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n` to efficiently calculate `2^n modulo p` without directly calculating `2^n`. The time complexity of this script is O(log n), which is more efficient than calculating `2^n` directly for large values of `n`.