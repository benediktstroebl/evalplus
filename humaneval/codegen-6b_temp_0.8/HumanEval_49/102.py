

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
    # The following code is faster than the recursive solution.
    if n == 0:
        return 1
    elif n % 2:
        return Modp(modp(n // 2, p), p) ** 2
    else:
        return modp(n // 2, p) ** 2
