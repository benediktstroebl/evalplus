

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

    n = str(bin(n))[2:]
    p = str(bin(p))[2:]
    n = '0' * (len(p) - len(n)) + n
    return sum([int(i) for i in n]) % 2

