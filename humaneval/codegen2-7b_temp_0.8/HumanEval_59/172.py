

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    n = abs(n)
    while not n % 2:
        n //= 2
    while not n % 3:
        n //= 3
    while not n % 5:
        n //= 5
    return n
