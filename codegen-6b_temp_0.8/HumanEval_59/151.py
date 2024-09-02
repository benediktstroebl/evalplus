

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n % 2 == 0:
        return 2
    else:
        maximum = n // 2
        for p in range(maximum, 2, -1):
            if n % p == 0:
                return p
