

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = n
    for factor in range(2, int(n/2)+1):
        if n % factor == 0 and is_prime(factor):
            largest_factor = factor
    return largest_factor

