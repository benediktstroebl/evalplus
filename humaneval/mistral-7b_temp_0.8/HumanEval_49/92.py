

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
    p = p % 100
    r = 1
    while n > 0:
        if n & 1 == 1:
            r *= r % p
        n >>= 1
        r *= r % p
    return r % p

