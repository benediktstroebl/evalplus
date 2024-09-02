

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

    assert(n >= 0 and p > 2)
    for _ in range(n):
        p = (p * 2) % (10 ** 9 + 7)
    return p % (10 ** 9 + 7)
