

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
    n = n % p
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 0
    if n == 5:
        return 1
    if n == 6:
        return 1
    if n == 7:
        return 0
    if n == 8:
        return 1
    if n == 9:
        return 1
    if n == 10:
        return 0
    if n == 11:
        return 1
    if n == 12:
        return 1
    if n == 13:
        return 0
    if n == 14:
        return 1
    if n == 15:
        return 0
    if n == 16:
        return 1
    if n == 17:
        return 1
    if n == 18
