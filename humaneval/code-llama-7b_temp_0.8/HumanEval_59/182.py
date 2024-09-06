

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 2
    while n > 1 and n % 2 == 0:
        largest = 2
        n //= 2
    while n > 1 and n % largest == 0:
        n //= largest
    largest = 3
    while n > 1 and n % largest == 0:
        largest = 6
        while n > 1 and n % largest == 0:
            n //= largest
    return n
