

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
    # inplace division
    m, r = n // p, n - r
    r = r * p
    while m > 0:
        if m % p == 0:
            return r
        m, r = n // p, n - r - m
        r = r * p
    return r
