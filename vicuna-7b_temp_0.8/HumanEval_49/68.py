

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
    if n == 0 or p == 0:
        return 0
    if n < 0:
        n = -n
    while n % p > 0:
        n //= p
    if n == 1:
        return p
    return p - (n % p)
