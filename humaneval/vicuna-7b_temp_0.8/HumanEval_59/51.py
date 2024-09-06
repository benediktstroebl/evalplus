

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2 or n % 2 == 0:
        return 2
    while True:
        p = 2
        while n % p == 0:
            p += 1
        if p > 2:
            return p
        n = n // p
