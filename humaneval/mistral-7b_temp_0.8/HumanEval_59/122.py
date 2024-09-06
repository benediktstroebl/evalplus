

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for candidate in range(2, n):
        if n % candidate == 0:
            if largest_prime_factor(candidate) == 1:
                return candidate
            else:
                return largest_prime_factor(candidate)

