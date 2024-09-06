

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
    if n == 0:
        return 1
    result = 1
    power = n
    while power > 0:
        if power & 1:
            result = (result * n) % p
        n = (n * n) % p
        power >>= 1
    return result

