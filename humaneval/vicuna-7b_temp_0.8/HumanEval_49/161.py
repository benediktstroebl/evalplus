

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
    # Check if p is even (for performance reasons)
    if p & 1 == 0:
        # To avoid overflows and performant modular exponentiation
        # We perform multiple modular operations
        # To speed up the modular exponentiation
        y = 1
        while n > 0:
            if n % p == 0:
                y = y * p % p
            n //= p
            if n % p == 0:
                y = y * p % p
            n //= p
        return y
    else:
        # p is odd
        x, y = 1, 1
        while n > 0:
            if n % p == 0:
                y = y * p % p
                n //= p
            x = (x * x) % p
            if n % p == 0:
                y = y * p % p
                n //= p
            x = (x * x) % p
        return y
