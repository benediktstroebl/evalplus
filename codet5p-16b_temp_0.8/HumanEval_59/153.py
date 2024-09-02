

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    prime_factors = []
    for x in range(2, n+1):
        if n % x == 0:
            prime_factors.append(x)
    largest_factor = max(prime_factors)
    return largest_factor

