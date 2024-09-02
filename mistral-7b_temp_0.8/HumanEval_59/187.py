

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # First find the smallest prime factor p of n.
    p = 2
    while n % p != 0:
        p += 1

    # Now find the largest factor of n that is divisible by p.
    while n % p == 0:
        n //= p

    return p

