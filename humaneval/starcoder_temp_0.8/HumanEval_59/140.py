

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        raise ValueError("Cannot take the largest prime factor of 1")
    return largest_prime_factor(n // largest_divisor(n))

