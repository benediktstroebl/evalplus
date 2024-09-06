

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
    # precondition: n >= 0, p > 0, p == 1 (mod 2)
    # assert n >= 0
    # assert p > 0
    # assert p & 1 == 1

    if n == 0:
        return 1
    if n == 1:
        return 2

    p2 = p * 2
    m = modp(n // 2, p2)
    m2 = (m * m) % p2
    if n % 2 == 0:
        return m2 % p
    else:
        return (m2 + m) % p

