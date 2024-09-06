

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
        n += p
    if n < 1:
        return 1
    if n == 1:
        return p - 1
    res = 1
    while n:
        if n % 2:
            res = res * p % p
        n >>= 1
        p = p * p % p
    return res

