

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
        raise ValueError("n should be non-negative")
    if p < 0:
        raise ValueError("p should be non-negative")
    if n == 0:
        return p
    while p > 0:
        if n % p == 0:
            return 0
        p, remainder = p // 101, p % 101
    return 1