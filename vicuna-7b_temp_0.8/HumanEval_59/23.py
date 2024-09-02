

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Note: This algorithm is not optimized for performance, only readability.
    # A more efficient implementation would likely involve binary search.
    p = 2
    while p <= n / p:
        p = p ** 2
    return p
