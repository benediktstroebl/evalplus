

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    prime_factor = n
    while prime_factor > 1:
        prime_factor = smallest_prime_factor(prime_factor)
    return prime_factor
