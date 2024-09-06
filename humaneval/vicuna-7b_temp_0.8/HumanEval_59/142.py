

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n > 1:
        p = 2
        while n % p == 0:
            p = p * p
        if p > 2:
            return p
        n = n // p
    return 2
