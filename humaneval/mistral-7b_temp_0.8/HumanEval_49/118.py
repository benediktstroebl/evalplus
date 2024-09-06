

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
    i = 1
    if i > p:
        return 1
    while True:
        if i == n:
            return i % p
        i *= 2
        if i > p:
            i %= p

