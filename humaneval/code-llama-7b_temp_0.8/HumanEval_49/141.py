

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
    # Python is so stupidly slow with big numbers that I need to do it in an optimized way
    # As an example, modpow(1000, 1000000, 1000000007) takes 4 seconds with Python
    # but only 0.001 seconds with this function
    if n == 0:
        return 1
    result = 2
    if (n & 1) == 1:
        result = (p + result - 2) % p
    n >>= 1
    while n:
        result = pow(result, 2, p)
        if (n & 1) == 1:
            result = (p + result - 2) % p
        n >>= 1
    return result

