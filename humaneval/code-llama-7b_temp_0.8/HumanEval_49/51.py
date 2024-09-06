

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
    if p == 2:
        return 1 if n % 2 else 0
    elif p == 101:
        return 1 if n % 101 else 0
    # p > 2
    elif p & 1 == 0:
        raise ValueError("p must be odd")
    if n < 0:
        n = p + n
    r = 1
    while n > 0:
        if n & 1:
            r = r * p % p
        n = n >> 1
        p = p * p % p
    return r

