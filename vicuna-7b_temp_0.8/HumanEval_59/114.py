

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p = 0
    while True:
        if n % 2 == 0:
            return 0
        if n % 3 == 0:
            return 0
        if n % 5 == 0:
            return 0
        p = 2
        while p < n // p:
            p = p + 6
        if n % p == 0:
            return p
        p += 2
    return 0