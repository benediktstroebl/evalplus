

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1 and n % 1 == 0, "n must be a positive integer greater than 1."
    prime_factors = []
    for factor in range(2, n + 1):
        if n % factor == 0:
            prime_factors.append(factor)
    return max(prime_factors)
