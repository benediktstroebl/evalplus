

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n = n // 2
    while n % 3 == 0:
        n = n // 3
    p = 5
    while n != 1:
        if n % p == 0:
            n = n // p
        else:
            p = p + 6
            if p > sqrt(n):
                return n


