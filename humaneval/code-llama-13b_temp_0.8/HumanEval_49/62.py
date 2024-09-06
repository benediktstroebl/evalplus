

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
    #assert isinstance(n, int)
    #assert isinstance(p, int)
    assert n >= 0
    assert p > 1
    v = 1
    while n > 0:
        v = (v * v) % p
        if n & 1:
            v = (v * 2) % p
        n = n >> 1
    return v

