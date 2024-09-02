

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError("n must be > 1")
    largest_factor = 0
    for i in range(2, n + 1):
        if i % n == 0:
            largest_factor = i
    return largest_factor

