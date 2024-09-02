

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
    #if not n < 0:
        if not n % 2:
            return p - 1
    if n < p:
        return 0
    if n >= p:
        return p - 1
    if n % 2 == 0:
        return (p - 1) // 2
    else:
        return (p - 1) // 2 + 1
