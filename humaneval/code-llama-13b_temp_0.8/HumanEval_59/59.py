

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Uncomment and implement
    for divisor in range(2, n+1):
        while n % divisor == 0:
            return divisor
    return n

