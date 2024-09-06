

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
    mask = 1
    while mask < p:
        mask *= 2
    while mask > 2:
        if (n & mask) == 0:
            mask /= 2
        else:
            return (mask + n) % p
    return mask

