

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if largest_prime_factor.is_prime(n):
        return n

    for i in range(2, n + 1):
        if largest_prime_factor.is_prime(i):
            if n % i == 0:
                return i

