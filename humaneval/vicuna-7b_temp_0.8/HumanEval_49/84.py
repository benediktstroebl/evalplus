

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
    # fast path for small values of n and p
    if n < 0 or p < 0:
        return 0
    elif n == 0:
        return p
    elif p == 0:
        return 1
    elif n % p == 0:
        return n // p
    elif p % 2 == 0:
        if n % p == 0:
            return (n // p) + (p // 2)
        else:
            return (n // p) - (p // 2)
    else:
        return (p - 1) // 2 - n % (p - 1)
