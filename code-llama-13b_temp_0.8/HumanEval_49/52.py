

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
    assert n >= 0 and p > 1
    mask = 1
    while mask < n:
        mask <<= 1
    mask >>= 1
    rval = 2
    while mask:
        rval = rval * rval
        if rval >= p:
            rval -= p
        if n & mask:
            rval = rval + 1
            if rval >= p:
                rval -= p
        mask >>= 1
    return rval

