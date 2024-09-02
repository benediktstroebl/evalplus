

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime = 2
    while n % prime == 0:
        n //= prime

    prime = 3
    while n % prime == 0:
        n //= prime

    prime += 2
    while prime * prime <= n:
        while n % prime == 0:
            n //= prime
        prime += 2

    return n

