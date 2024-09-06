

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
    a = 2
    b = p
    if n == 0:
        return 1
    for _ in range(n-1):
        a = (a**2 - 1) % b
    return a
