```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the mathematical property that for any prime p and any integer n:
    2^(p-1) ≡ 1 (mod p)
    Therefore, we can use the property of modular exponentiation to efficiently compute 2^n mod p.

    :param n: The exponent.
    :param p: The modulus.
    :return: The result of 2^n modulo p.
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
    if p == 1:
        return 0
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result
```

This function takes advantage of the property of modular exponentiation to efficiently compute 2^n mod p. It works by repeatedly squaring the base and reducing the result modulo p, until the exponent n is zero. If n is odd, it multiplies the result by the base before reducing it modulo p. This approach ensures that the intermediate results do not exceed the range that can be represented by Python's integers, even for large values of n and p.