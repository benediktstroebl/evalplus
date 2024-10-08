

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1 and n % 2 == 0, "Assumed n > 1 and is not a prime"

    return max(filter(lambda x: n % x == 0, range(3, n, 2)))

