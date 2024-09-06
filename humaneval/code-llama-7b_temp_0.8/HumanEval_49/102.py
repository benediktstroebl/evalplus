

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
    n %= p
    if n == 0:
        return 1
    power = 2
    while power <= n:
        n, remainder = divmod(n, power * 2)
        if remainder:
            return power + modp(n, p)
        power *= 2
    return n + 1

