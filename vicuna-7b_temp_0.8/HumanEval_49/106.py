

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
    # use binary exponentiation with a bit of optimization
    exp = n - 1
    if exp >= p:
        return (p**exp) % p
    if exp % 2 == 1:
        return (p * (p - 1) * (p - 2)) % p
    # (p - 1)**2 = (p - 1) \* (p - 1) = p - 1, so the above returns p - 1
    # and the below returns p - 1%p = (p - 1)%p
    return ((p - 1)**2) % p
