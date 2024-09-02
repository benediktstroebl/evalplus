

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
    # Compute a, b, r, d such that a^d (mod p) = b^r (mod p)
    a, b, r, d = 1, 1, 0, n // 2
    while p - d < 0:
        d //= p
        a, b, r, d = b, a, r + 1, d // p

    # Compute 2^n = a^r (mod p)
    r = r // 2
    if r == 1:
        r = 0
    i = (r + 1) // 2
    return pow(a, i, p) % p
