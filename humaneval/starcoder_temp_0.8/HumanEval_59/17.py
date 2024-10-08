

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    factor = 2
    while n > 1:
        factor = smallest_divisor(n)
        n = n // factor
    return factor
