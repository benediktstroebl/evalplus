

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
    assert p > 1
    if n < 0:
        return modp(-n, p)
    if p == 2:
        return 1 if n & 1 else 0

    x, y = 1, 0
    while n:
        if n & 1:
            x, y = (x * p + y) % p, x
        n >>= 1
        p *= p
    return x

