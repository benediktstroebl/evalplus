

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
    mask = 1
    r = 0
    while mask < p:
        if n & mask:
            r = (r + mask) % p
        mask <<= 1
    return r

