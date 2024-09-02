

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    while n % 3 == 0:
        prime_factors.append(3)
        n = n // 3

    while n % 5 == 0:
        prime_factors.append(5)
        n = n // 5

    while n % 7 == 0:
        prime_factors.append(7)
        n = n // 7

    return max(prime_factors)

