

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    if n % 2 == 0:
        return 2
    while True:
        if n % 3 == 0:
            return 3
        if n % 2 == 0:
            return 2
        n = n - 2
