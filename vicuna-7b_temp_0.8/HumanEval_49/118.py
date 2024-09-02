

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
    # Numerics
    if not (0 <= n <= p - 1):
        raise ValueError("n must be between 0 and p-1")
    if not (0 <= p <= 2**31):
        raise ValueError("p must be a 32-bit integer")
    if not (0 <= n % p):
        raise ValueError("n must be co-prime with p")
    if not (0 <= p % 2):
        raise ValueError("p must be odd")

    if n == p - 1:
        return 1
    if n == p:
        return 0
    r = 1
    for i in range(p-1, -1, -1):
        if n % i == 0:
            return 0
        r = r * i % p
    return r
