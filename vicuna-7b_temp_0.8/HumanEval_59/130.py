

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError(f"n must be at least 2: {n}")
    if n % 2 == 0:
        return 2
    while n > 1:
        if n % 2 == 1:
            d = n // 2
            if d > 1:
                n = d
            else:
                n = 2
        else:
            d = n // 3
            if d > 1:
                n = d
            else:
                n = 3
    return n