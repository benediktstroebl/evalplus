

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
    if n < 0 or p < 0:
        raise ValueError("n and p must be non-negative integers")
    if n == 0:
        return p if p > 0 else 1
    if n % 2 == 0:
        q = (p - 1) // 2
        if n < q:
            return 1
        else:
            return 0
    if n % 2 == 1:
        q = (p - 1) // 2
        if n < q:
            return 0
        else:
            return 1
    if n < p:
        return 0
    return p
