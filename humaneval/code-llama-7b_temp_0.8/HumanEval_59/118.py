

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n % 2 == 0:
        return 2
    factor = 3
    while factor ** 2 < n:
        if n % factor == 0:
            return factor
        factor += 2
    return n

