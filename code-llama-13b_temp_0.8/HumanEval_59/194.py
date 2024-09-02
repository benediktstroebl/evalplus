

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    """Begin Pseudocode"""
    """
    1. Make a list of all prime factors using sieve_of_eratosthenes(n)
    2. Return the last element of the list
    """
    return sieve_of_eratosthenes(n)[-1]
