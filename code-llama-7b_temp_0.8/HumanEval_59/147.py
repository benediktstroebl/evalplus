

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for x in range(int(n ** .5), 1, -1):
        if n % x == 0:
            while n % x == 0:
                n //= x
            return x
    return n

