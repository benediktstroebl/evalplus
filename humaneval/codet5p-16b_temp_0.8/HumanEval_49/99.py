

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

    assert n >= 0 and p > 2
    a, b = 1, 1
    for i in range(n):
        a, b = (a * 2) % p, (a + b * 2) % p
    return a

