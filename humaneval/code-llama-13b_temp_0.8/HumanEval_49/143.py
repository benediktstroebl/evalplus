

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
    if not n:
        return 1
    if n & 1:  # if n is odd
        return (2 * modp(n - 1, p)) % p
    # otherwise n is even
    return (modp(n // 2, p) * modp(n // 2, p)) % p

