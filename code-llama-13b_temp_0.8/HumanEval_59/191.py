

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 2
    while n % largest_prime == 0:
        n = n // largest_prime
        largest_prime = 2
    factor = 3
    while n > 1:
        if n % factor == 0:
            largest_prime = factor
        factor += 2
        while n % factor == 0:
            n = n // factor
    return largest_prime

