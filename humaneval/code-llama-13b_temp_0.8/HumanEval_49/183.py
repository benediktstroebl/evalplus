

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
    r = 1
    if n == 0:
        return r
    if n == 1:
        return (r * 2) % p
    b = 1
    while b <= n:
        b *= 2
        if b <= n:
            r = (r * r) % p
    return r

