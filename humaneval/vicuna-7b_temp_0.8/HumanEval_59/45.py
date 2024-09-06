

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n >= 2:
        if n % 2 == 0:
            return 2
        elif n % 3 == 0:
            return 3
        elif n % 2 == 1 and n % 4 == 0:
            return 4
        elif n > 15:
            n = n - 1
    return 1
