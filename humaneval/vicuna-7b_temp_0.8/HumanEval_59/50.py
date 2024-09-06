

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the prime factorization of n and extract the largest prime factor
    factors = factor(n)
    largest_prime = int(n)
    for factor in factors.keys():
        if factor > largest_prime:
            largest_prime = factor
    return largest_prime
