

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
    assert p > 0

    # the modulus cannot be zero
    if n == 0:
        return 1

    # we can use one of the following:
    # 1. binary exponentiation (recursion)
    # 2. iterative algorithm

    # base case
    if n == 1:
        return 2

    # recursion
    res = modp(n // 2, p)
    res = (res ** 2) % p
    if n % 2:
        res = (res * 2) % p

    return res

