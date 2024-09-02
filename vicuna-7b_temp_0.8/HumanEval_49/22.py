

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
    # if n is negative, add it to the end of p
    if n >= 0:
        return pow(2, n, p) % p
    else:
        p_plus_one = p + 1
        while p_plus_one <= p:
            if pow(2, n, p_plus_one) == p_plus_one:
                return pow(2, n, p_plus_one) % p
        return 1
