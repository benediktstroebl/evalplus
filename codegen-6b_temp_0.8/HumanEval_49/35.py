

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
    if n == 0:
        return 1
    elif p == 1:
        raise ValueError('0 and 1 are the only possible values for p')
    elif p == 2:
        return n
    else:
        return modp(n, p >> 1) * (n ^ modp(p >> 1, p)) % p