

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
    assert n >= 0 and p > 0, "n and p must be nonnegative"
    for i in range(1, n + 1):
        if (n + 1) % i == 0 and i % p == 0:
            return int(i)
    assert False, "n is not in the range 0 to p-1"
