

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for k in range(n - 1, 1, -1):
        if n % k == 0:
            return k
    return 1  # return 1 if n is a prime

