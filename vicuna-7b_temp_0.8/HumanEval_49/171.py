

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
    res = 1
    while p > 0:
        if n % p == 0:
            return p
        n //= p
        p = p - 1
        res = res * p + n // p
    return 1
