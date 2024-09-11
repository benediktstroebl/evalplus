```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
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
        # If n is odd, multiply the current result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result
```

This function uses the property of modular arithmetic that `(a * b) % n = ((a % n) * (b % n)) % n` to avoid large intermediate results. It also uses the property that `a^n % n = ((a % n)^n) % n` to reduce the exponent `n` to its remainder when divided by `p-1`, which is the period of 2^n modulo p.