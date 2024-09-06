

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
    # make sure n is not zero
    if n == 0:
        return 0

    # handle the case of p-1 being zero
    while p % 2 == 0:
        p = p // 2
        n = n - 1

    # calculate 2^n modulo p
    result = pow(2, n, p)
    return result
