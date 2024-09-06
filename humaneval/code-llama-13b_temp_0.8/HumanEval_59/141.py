

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime = 1
    for divisor in range(2, n):
        if n % divisor == 0:
            prime = divisor
    return prime

