

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 1
    while n % 2 == 0:
        largest = 2
        n //= 2
    while n % 3 == 0:
        largest = 3
        n //= 3
    d = 5
    while n != 1:
        while n % d != 0:
            d += 6
        largest = d
        n //= d
        d += 6
    return largest

