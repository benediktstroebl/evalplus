

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
    while n % 5 == 0:
        n = n // 5

    for i in range(7, int(n ** 0.5) + 1, 6):  # only test odd numbers
        if n % i == 0:
            n = n // i
        elif n % (i + 2) == 0:
            n = n // (i + 2)
    return n

