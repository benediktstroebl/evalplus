

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            largest_prime = d
            n //= d
        if n == 1:
            return largest_prime
        d = d + 1
    return n

