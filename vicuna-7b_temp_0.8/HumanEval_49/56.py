

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
    # if n < 0, n = -n
    if n < 0:
        n = -n
    # if p = 0, return 1
    if p == 0:
        return 1
    # if p = 1, return 2
    if p == 1:
        return 2
    # if n = 0, return 0
    if n == 0:
        return 0
    # n = n/p + (n%p != 0)
    quotient = n // p
    remainder = n % p
    # return 2**(n/p) mod p
    return 2**quotient % p
