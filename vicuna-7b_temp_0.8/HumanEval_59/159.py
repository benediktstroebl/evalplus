

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Try to factor n using a trial factoring method
    factors = trial_factors(n)
    # If no prime factors are found, then the largest prime factor is 2
    if not factors:
        return 2
    # If some prime factors are found, the largest one is the largest
    for factor in factors:
        if factor > n:
            return factor
    # If no prime factors are found, return 2 as a placeholder value
    return 2