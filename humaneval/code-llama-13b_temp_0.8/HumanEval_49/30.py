

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
    # return 2**n % p
    # return pow(2, n, p)
    base = 2
    if base**(n+1) % p != base:
        return base**n % p

    # bit shift
    # return (base**(n-1) % p << 1) % p
    return (pow(base, n, p) << 1) % p

