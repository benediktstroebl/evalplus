

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
    # handle negative n
    if n < 0:
        n = -n
    # handle small n
    if n < 16:
        return n
    # compute n! % p
    r = 1
    for i in range(1, n+1):
        r *= i
    # compute 2^n % p
    return (r // 2) % p