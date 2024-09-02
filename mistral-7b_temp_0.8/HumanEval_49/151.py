

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
    assert p > 1 and n >= 0, "bad n,p"
    assert p & -p == p, "p is not power of 2"
    if n == 0:
        return 1
    if p & 1 == 0:
        return modp(n >> 1, p >> 1)
    return (modp(n >> 1, p >> 1) * modp(n >> 1, p >> 1)) % p

