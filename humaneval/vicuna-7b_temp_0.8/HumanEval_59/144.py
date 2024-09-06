

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n > 1 and n % 2 == 0:
        n = n // 2
    while n > 3 and n % 3 == 0:
        n = n // 3
    while n > 7 and n % 7 == 0:
        n = n // 7
    while n > 11 and n % 11 == 0:
        n = n // 11
    return n