

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        return 1
    while n % 2 == 0:
        n = n // 2
    if n > 3:
        return n
    # n is prime, so return 1
    return 1
