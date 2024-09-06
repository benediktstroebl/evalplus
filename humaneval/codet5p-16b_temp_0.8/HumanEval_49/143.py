

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

    assert n >= 0, f'{n} must be positive'
    assert p > 2, f'{p} must be at least 3'
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (2 * modp(n // 2, p)) % p
    else:
        return (modp(n - 1, p) ** 2) % p

