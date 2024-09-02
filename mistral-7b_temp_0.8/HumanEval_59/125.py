

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # First, find the smallest prime factor
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            factor = 2
        else:
            factor += 1
    return n

