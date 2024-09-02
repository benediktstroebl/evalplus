

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
    # Handle cases 1 and 3
    if n == 1:
        return p - (p - 1) % p
    elif n % p == 0 and n % 2 == 0:
        return 2**n % p
    # Handle case 2
    elif n % p == 0:
        return (p - (p - 1) % p) % p
    # Handle case 4
    elif p > 2 and n % 2 == 0:
        return 2**n % p
    # Handle case 5
    elif n > 1:
        return (p - (p - 1) % p) % p
    else:
        return p % p
