

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
    if n < 0:
        n = n + p
    if n == 0:
        return p - 1
    if p == 2:
        return n % 2
    m = 1
    while n > 0:
        m = (m * 2) % p
        n = n >> 1
    return m
