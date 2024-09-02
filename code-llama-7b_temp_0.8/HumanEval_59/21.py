

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
    i = 5
    while i * i <= n:
        while n % i == 0:
            n = n // i
        while n % 5 == 0:
            n = n // 5
        i = i + 6
    return n

