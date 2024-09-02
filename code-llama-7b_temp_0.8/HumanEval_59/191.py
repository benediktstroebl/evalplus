

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Distinct prime factors are greater than 1
    # So we can loop from 2 to sqrt(n)
    # If n is divisible by i, then n is not a prime
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
        i = i + 1
    return n

