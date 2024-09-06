

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

    b = bin(n)[2:]
    r = pow(2, len(b) - 1, p)
    for i in range(len(b) - 2, -1, -1):
        if b[i] == "1":
            r = (r * 2) % p
        r = (r * 2) % p
    return r

