

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_prime = n - 1
    while max_prime > 1:
        if n % max_prime == 0:
            return max_prime
        max_prime -= 1
    return 1

