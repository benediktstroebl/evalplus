

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        return 0
    if n % 2 == 0:
        return 2
    prime = 3
    while prime <= n // prime:
        if n % prime == 0:
            n /= prime
        else:
            prime += 2
    return n
