

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = prime_factors(n)

    # Find the largest prime factor
    max_factor = 1
    for factor in factors:
        max_factor = max(max_factor, factor)

    return max_factor

