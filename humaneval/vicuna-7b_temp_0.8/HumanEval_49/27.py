

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
    if n < 0:
        raise ValueError("n must be non-negative")
    if p < 0:
        raise ValueError("p must be non-negative")
    if n == 0:
        return 1
    if p > 0 and n % p == 0:
        return 1
    result = (n // p) % p
    if n % p != 0:
        result += (p - (n % p)) % p
    return result
