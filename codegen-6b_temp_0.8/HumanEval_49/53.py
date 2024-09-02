

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
    res = n % p
    if p == 1:
        raise Exception('P is 1')
    elif res == 0:
        return p
    elif res == 1:
        return p - 1
    elif res == p - 1:
        return 0
    else:
        return res

