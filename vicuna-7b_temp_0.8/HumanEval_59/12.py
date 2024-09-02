

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if not n > 1 or n % 2 == 0:
        return 1
    while True:
        if n % 2 == 0:
            n = 2 * n + 1
        if n % 3 == 0:
            n = 3 * n + 1
        if n % 5 == 0:
            n = 5 * n + 1
        if n % 7 == 0:
            n = 7 * n + 1
        if n > 1:
            return n
