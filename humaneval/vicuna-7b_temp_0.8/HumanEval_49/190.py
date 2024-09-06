

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
    n, p = abs(n), abs(p)
    if n <= 0 or p <= 0:
        return 0
    while p > 0:
        if n % p == 0:
            return n
        n //= p
        p = p - 1
    return p - 1
