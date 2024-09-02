

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
    assert n >= 0, n
    assert p > 1, p

    # 2^n mod p
    if n == 0:
        return 1

    # compute 2^k mod p
    temp = modp(n >> 1, p)
    temp2 = temp * temp % p
    if n & 1:  # n is odd, then temp^2 * 2
        return temp2 * 2 % p
    else:  # n is even, then temp^2
        return temp2

