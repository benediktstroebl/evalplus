```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.

    Examples:
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
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # n is even, divide n by 2
        n = n // 2
        # Update the base to be the square of the current base (because 2^(2k) = (2^k)^2)
        base = (base * base) % p
    return result
```

This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n` to avoid large intermediate results. It also uses the property that `2^(2k) = (2^k)^2` to efficiently compute powers of 2 modulo p by squaring the base.