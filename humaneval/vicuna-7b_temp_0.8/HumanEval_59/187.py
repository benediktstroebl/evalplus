

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be at least 2")
    if n % 2 == 0:
        raise ValueError("n must not be even")
    i = 0
    while n > 3:
        if n % i == 0:
            n = n / i
        i += 1
    return i
