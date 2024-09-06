

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
    # Check if n is 0
    if n == 0:
        return 1
    # Check if n is a power of 2
    if n % 2 == 0:
        return 1
    # Calculate (n - 1) % p
    t = n - 1
    while t >= p:
        t -= p
    # Calculate 2^(t) % p
    return pow(2, t, p) % p
