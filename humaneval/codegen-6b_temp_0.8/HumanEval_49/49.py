

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
    # (return (n % p) + p) % p
    if (n == 0):
        return ((n % p) + p) % p
    elif (n == 1):
        return 1
    elif (n == 2):
        return (2 % p)
    elif (n == 3):
        return (3 % p)
    elif (n == 4):
        return (2 % p)
    elif (n == 5):
        return (4 % p)
    elif (n % 2 == 0):
        return modp(n//2, p) % p
    else:
        return (n % p) + p


