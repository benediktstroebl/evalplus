

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
    # get value of 2^n
    two_to_the_n = 2**n % p
    if two_to_the_n == 0:
        two_to_the_n = p
    return two_to_the_n
