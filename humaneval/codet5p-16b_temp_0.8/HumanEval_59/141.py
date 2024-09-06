

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    factor = n - 1 # Assume n is not a prime
    while n % factor!= 0:
        factor = factor - 1
    return factor
