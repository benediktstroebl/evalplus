

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
    n, p = (int(n), int(p))
    # First we check n is a nonnegative integer.
    if n < 0:
        raise ValueError("n must be nonnegative")
    # Second, we check that n is not too large (only the exponent, not the base).
    if 2**n > p:
        raise ValueError("n must be less than the bit length of the modulus")
    # Now we compute 2^n mod p.
    n = n % p  # guaranteed to be nonnegative
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
    return result

