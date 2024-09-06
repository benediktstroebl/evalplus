

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1 and isinstance(n, int), "Assert error: n should be a positive integer."
    largest_prime_factor = 0
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                largest_prime_factor = i
    return largest_prime_factor
