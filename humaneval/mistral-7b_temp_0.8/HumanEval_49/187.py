

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
    assert p > 1
    assert n >= 0
    x, y = 0, 1
    while n > 0:
        if n & 1:
            x, y = x + p * y, y
        n = n >> 1
        y = y + y
    return x % p

