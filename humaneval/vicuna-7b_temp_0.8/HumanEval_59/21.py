

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return 1
    if n == 2:
        return 2
    d = 2
    while d <= int(n**0.5) and d != n//d:
        d = 2
    return d