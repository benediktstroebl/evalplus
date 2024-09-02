

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = set(range(2, n + 1))
    while len(factors) > 1:
        factor = factors.pop()
        if n % factor == 0:
            n //= factor
            factors.discard(factor)
    return factor

