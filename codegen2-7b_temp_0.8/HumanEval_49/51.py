

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
    if p == 2:
        return (n & 1) ^ 1
    if p == 3:
        return (n & 1) ^ 1
    if p == 5:
        return (n & 3) ^ 1
    if p == 7:
        return (n & 1) ^ 1
    if p == 11:
        return (n & 3) ^ 3
    return pow(n, p-2, p
