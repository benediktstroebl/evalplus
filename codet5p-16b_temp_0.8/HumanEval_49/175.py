

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
        raise ValueError("Value must be non-negative: %d" % n)
    if p < 2:
        raise ValueError("Value must be non-negative: %d" % p)
    a, b = n, p
    x, y = 1, 0
    while b:
        a, (q, b) = b, divmod(a, b)
        x, y = y, x - q * y
    if x < 0:
        x += p
    return x
