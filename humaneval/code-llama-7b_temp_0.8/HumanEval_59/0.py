

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_prime_factor = 1
    i = 2
    while n % i != 0:
        i = i + 1
    max_prime_factor = i
    return max_prime_factor

