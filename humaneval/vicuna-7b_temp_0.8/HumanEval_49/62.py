

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
    d, r = 0, p - 1
    while n > 0:
        n, d = d * 10 + n % p, d // 10
        r, p = modp(p - r, p), p + r % p
    return d
