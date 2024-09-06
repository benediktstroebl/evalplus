

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

    n = bin(n)[2:]  # remove '0b'
    while len(n) < p:  # append leading zeros
        n = '0' + n
    n = n[-p:]  # remove trailing zeros
    n = int(n, 2)
    return n

