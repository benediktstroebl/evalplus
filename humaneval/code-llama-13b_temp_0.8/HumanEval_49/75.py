

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
    if n < 0:
        return modp(-n, p)
    if n == 0:
        return 1
    if n == 1:
        return 2

    # Make sure we have a power of two.
    n -= 1
    while n % 2 == 0:
        n //= 2

    # Find an exponent for 2 that is not too large.
    i = 0
    while (2 << i) <= p:
        i += 1
    # Take a few steps to get in range.
    for _ in range(i - 2):
        n = (n << 1) % p
    # Now do the exponentiation.
    while n:
        if n % 2 == 1:
            n = (n * 2) % p
            result = (result * 2) % p
        n //= 2
        result = (result * result) % p
    return result

