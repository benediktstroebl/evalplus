

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # p is the largest prime factor
    p = 1
    d = 2
    # Find largest prime factor
    while d * d <= n:
        while n % d == 0:
            p = d
            n = n // d
        d = d + 1
    # If n is prime, then n = p
    if n > 1:
        p = n
    return p

