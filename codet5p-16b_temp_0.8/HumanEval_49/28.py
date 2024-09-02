

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

    assert 0 <= n < p
    assert 2 <= p
    if n == 0: return 1
    if n == 1: return 2
    a = modp(n-1, p)
    return (a*a) % p

