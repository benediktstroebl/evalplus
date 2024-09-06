

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be a positive integer > 1")
    max_divisor = 2
    while (max_divisor * max_divisor <= n):
        if n % max_divisor == 0:
            n = n // max_divisor
        else:
            max_divisor += 1
    return n

