

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
        return -modp(-n, p)
    if n == 0:
        return 1
    acc = 2
    for _ in range(n):
        acc = (acc * acc) % p
    return acc
