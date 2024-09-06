

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
    # check if n >= 0 and n < p
    if n >= 0 and n < p:
        if n % 2 == 0:
            return p - (p // n)
        else:
            return p - (p // (n - 1))
    # if n is negative, return 0
    else:
        return 0
