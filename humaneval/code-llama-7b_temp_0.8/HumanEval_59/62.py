

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    assert n > 1
    max_prime_factor = 2
    while n % 2 == 0:
        n = n // 2
        max_prime_factor = 2
    while n % max_prime_factor != n:
        max_prime_factor += 1
        while n % max_prime_factor == 0:
            n = n // max_prime_factor
    return max_prime_factor

