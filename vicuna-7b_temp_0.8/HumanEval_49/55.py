

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
    if n < 0 or p < 0:
        raise ValueError("n and p must be non-negative integers")
    if n == 0:
        return p
    if p == 0:
        raise ValueError("p cannot be zero")
    return pow(2, n, p) % p
