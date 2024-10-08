

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
    assert n >= 0
    if n < 32:
        v = 1
        for _ in range(n):
            v = (v << 1) % p
        return v
    x = 1 << n // 2
    y = x << (n - n // 2)
    return modp(x, p) * modp(y, p) % p

