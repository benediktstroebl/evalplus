

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # if n < 3, it can't be prime, so we return its own prime factor
    if n < 3:
        return n
    # use trial division to find the largest prime factor of n
    # this is O(sqrt(n)) in time complexity
    for p in prime_factors(n):
        if p > n // (n // p):
            return p
    return None  # no prime factor was found
