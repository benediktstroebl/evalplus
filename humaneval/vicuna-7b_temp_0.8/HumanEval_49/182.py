

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
    # Check for overflow
    if n > 31 or p > 10000000000000000000000000000000000000000000000000000000000001:
        raise OverflowError

    if p > n:
        return 0

    return ((n // p) * p) % p
