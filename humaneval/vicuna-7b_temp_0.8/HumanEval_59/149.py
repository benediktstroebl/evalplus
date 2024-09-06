

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Try to find a prime factor of n using trial division
    for i in range(2, n):
        if n % i == 0:
            return i
    # If n is not divisible by any prime, it must be composite
    # so the largest prime factor is n itself
    return n
