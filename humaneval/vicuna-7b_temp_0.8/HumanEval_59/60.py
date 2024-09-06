

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is a prime
    if n > 1 and n % 2 == 0:
        return 2
    # check if n is a power of 2
    if n == 0 or n == 1:
        return 1
    # find the largest prime factor
    d = 2
    while d <= n // d:
        if n % d == 0:
            return d
        d += 2
    return n // d + 1  # 
