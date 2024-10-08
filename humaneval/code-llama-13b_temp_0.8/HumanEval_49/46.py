

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
    assert n >= 0
    assert p >= 2
    r = 1
    b = 2
    while n:
        if n & 1:
            r = r * b % p
        b = b * b % p
        n >>= 1
    return r

