

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
    bin_n = bin(n)[2:]
    if len(bin_n) < p:
        bin_n = '0'*(p-len(bin_n)) + bin_n

    return int(bin_n[-p:], 2)
