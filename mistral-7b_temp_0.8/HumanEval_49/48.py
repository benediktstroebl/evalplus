

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
    p = p % 100
    x, y = 1, 0
    while n > 0:
        n, k = n // 2, n % 2
        x, y = x * x, y * (2 * x + y)
        if k == 1:
            x, y = x * x, y * (2 * x + y)
    return y % p

