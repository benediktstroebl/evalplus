

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
    # fast case: p is prime and n is <= 20
    if (p > 0) and (p not in _PRIMES) and (n <= 20) and (n not in _PRIMES):
        if n == 0:
            return 1
        elif p % n == 0:
            return 0
        else:
            return p // n
    else:
        # standard case: p is composite and n > 20
        phi = (p - 1) // 2
        q = p // 2
        while q < n:
            if n % q == 0:
                return 0
            q //= 2
        return p - 1
