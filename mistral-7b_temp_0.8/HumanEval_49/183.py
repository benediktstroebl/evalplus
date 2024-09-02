

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
    n = (n % (p - 1)) if n < p else (n % (p - 1) + p - 1) % (p - 1)
    x = 1
    while n > 0:
        if n & 1:
            x = x * 2 % p
        n >>= 1
        x = x * x % p
    return x

