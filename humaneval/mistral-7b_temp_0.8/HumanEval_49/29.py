

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
    x = 1
    for i in range(n):
        if i < n // 2:
            x = x * 2 % p
        else:
            x = x * 2 % p
            x = x * x % p
    return x

