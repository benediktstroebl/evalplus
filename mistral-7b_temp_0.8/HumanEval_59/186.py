

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return 0
    for factor in range(2, n):
        if n % factor == 0:
            if largest_prime_factor(n // factor) == factor:
                return factor
            else:
                return largest_prime_factor(n // factor)

