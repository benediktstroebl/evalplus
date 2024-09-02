

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
    assert isinstance(n, int), n
    assert isinstance(p, int), p
    assert p > 1, p
    r = 1
    a = 2
    while n:
        if n & 1:
            r = (r * a) % p
        a = (a * a) % p
        n >>= 1
    return r

