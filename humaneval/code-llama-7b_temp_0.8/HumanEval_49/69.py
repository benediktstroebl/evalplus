

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
    # 2^n mod p = (p^n - 1) / (p-2)
    # so, if p-2 is multiple of n
    # we just need to return p^n - 1
    if (p - 2) % n == 0:
        return (p ** n) - 1
    # if p-2 is not multiple of n,
    # we need to find m such that (p-2) * m = n
    m = n
    while m % n != 0:
        m += p - 2
    return (p ** n) - 1 // m

