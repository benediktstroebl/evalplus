

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
    if n <= 0:
        return 0
    if p <= n % p:
        return 1
    r = (n % p) // 2
    while p % 2:
        r = (r + n // p) // 2
        n = n // p
    return r + n % p