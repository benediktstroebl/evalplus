

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 2 == 1:
        for x in range(5, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return x
        return 5
    else:
        for x in range(7, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return x
        return 7
