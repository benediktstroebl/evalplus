

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
    a, b = p - 1, n
    if b < a:
        return 1
    while b >= a:
        b -= a
        n = n // 2
        a = a - 1
    return n