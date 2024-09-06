

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
    n, p = n % p, p
    if n <= 0:
        return 0
    if n == 1:
        return p
    while n % 2 == 0:
        n = n // 2
        p = p - 1
    return p * p + n
