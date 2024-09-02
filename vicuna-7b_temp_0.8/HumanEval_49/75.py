

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
    n, p = max(n, p), min(n, p)
    r = 0
    d = p - 1
    while n > 0:
        n, d = d, d % n
        r = r * n + d
    return r % p
