

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the largest prime that is less than or equal to n/2
    if n % 2 == 0:
        n += 1
    p = 2
    while n % p == 0:
        p += 2
    while p * p <= n:
        p += 2
    return p - 1