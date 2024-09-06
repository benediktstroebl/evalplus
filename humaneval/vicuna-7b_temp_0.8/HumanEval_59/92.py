

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Avoid prime numbers less than 3
    if n < 3:
        return n
    # find the number's prime factors
    factors = factor(n)
    largest_factor = 1
    for factor in factors:
        if factor > n // factor:
            largest_factor = max(largest_factor, factor)
    return largest_factor
