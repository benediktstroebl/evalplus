

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
        raise ValueError("n must be non-negative")
    if p < 2:
        raise ValueError("p must be greater than 2")
    if not p % 2:
        return p - p // 2
    x = ((p - 1) // 2) * p
    if n % 2 == 1:
        return (x + (p // 2)) // p
    else:
        return (x + (p // 2) + p // 4) // p
