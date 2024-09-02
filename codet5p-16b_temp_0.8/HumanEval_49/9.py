

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

    assert 0 <= n
    assert p > 1
    if p == 2:
        return 1 if n % 2 == 1 else 0
    m = p - 1
    z = 1
    while m % 2 == 0:
        m //= 2
        z *= 2
    r = modp(n, m)
    return r if r < z else r - z

