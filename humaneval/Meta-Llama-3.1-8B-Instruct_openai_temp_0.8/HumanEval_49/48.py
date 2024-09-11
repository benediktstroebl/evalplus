```python
def modp(n: int, p: int):
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
        # Check if n is odd
        if n % 2 == 1:
            # If n is odd, multiply result by base
            result = (result * base) % p
        # Update n and base for the next iteration
        n = n // 2
        base = (base * base) % p
    return result
```

This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n` to avoid large numbers, and the fact that `2^2 % n` is faster to compute than `2^n % n` to reduce the number of multiplications. It uses a while loop to efficiently compute the result for large exponents.