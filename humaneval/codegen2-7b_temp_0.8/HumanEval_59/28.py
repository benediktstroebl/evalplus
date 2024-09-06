

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0 and n!= 2:
        n = n // 2
    for x in range(3, int(n**0.5) + 1, 2):
        while n % x == 0:
            n = n // x
    return n

