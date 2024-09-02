

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = prime_factorize(n)
    return max(prime_factors, key=prime_factors.get) if len(prime_factors) > 0 else None

