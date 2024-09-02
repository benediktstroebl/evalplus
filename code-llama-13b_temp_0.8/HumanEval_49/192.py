

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
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")

    if p <= 0:
        raise ValueError(f"p must be positive, got {p}")

    r = 1
    for _ in range(n):
        r *= 2
        if r >= p:
            r -= p
    return r

