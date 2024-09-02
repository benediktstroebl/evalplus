

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    while n % 2 == 0:
        n = n // 2

    prime = 3
    while prime <= math.sqrt(n):
        while n % prime == 0:
            n = n // prime

        prime = prime + 2

    return n
