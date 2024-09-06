

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
    # check overflow
    if n < 0:
        return 0
    if n == 0 and p == 0:
        return 1
    if p < 0:
        raise ValueError
    result = pow(2, n, p)
    if n > 0 and p % n == 0:
        return result
    if n < 0:
        return 1 - result
    if n == 0:
        return 1
    while p % n == 0:
        p //= n
        n -= 1
    return result