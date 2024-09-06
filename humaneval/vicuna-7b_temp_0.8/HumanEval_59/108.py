

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    
    d = 0
    while n > 1:
        d = (n % 2) + (d + 1) // 2
        n = 2 * n // d
    return d
