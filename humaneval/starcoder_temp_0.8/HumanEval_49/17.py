

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
    n, p = int(n), int(p)
    a = 1
    while n > 0:
        if n & 1:
            a = a * p % p
        p = p * p % p
        n >>= 1
    return a
