

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for prime in range(2, 11):
        if n % prime == 0:
            n = n // prime
            return prime

    for prime in range(11, 32):
        if n % prime == 0:
            n = n // prime
            return prime

    return largest_prime_factor(n)

