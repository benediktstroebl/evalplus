

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    while n % 7 == 0:
        n = n / 7
    while n % 11 == 0:
        n = n / 11
    while n % 13 == 0:
        n = n / 13
    while n % 17 == 0:
        n = n / 17
    while n % 19 == 0:
        n = n / 19
    while n % 23 == 0:
        n = n / 23
    while n % 29 == 0:
        n = n / 29
    while n % 31 == 0:
        n = n / 31
    return int(n)

