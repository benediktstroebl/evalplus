

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 2 == 1:
        for i in range(5, int(n**0.5) + 1, 2):
            if n % i == 0:
                return i
        return 5
    for i in range(7, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return 7
