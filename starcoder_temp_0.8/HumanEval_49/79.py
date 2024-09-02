

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
    assert n >= 0 and p > 0 and (p & (p - 1)) == 0
    res = 1
    while n:
        if n & 1:
            res = (res * p) % p
        p = (p * p) % p
        n >>= 1
    return res

