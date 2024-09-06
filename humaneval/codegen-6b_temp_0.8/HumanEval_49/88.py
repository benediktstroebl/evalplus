

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
    assert n >= 0 and p >= 2 and p % 2 != 0, 'modp() p must be >=2 and p must be odd'
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (modp(n // 2, p)**2) % p
    else:
        return (modp(n - 1, p) * p) % p

