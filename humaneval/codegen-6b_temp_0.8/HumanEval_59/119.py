

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    multiplier = 2
    while n > 1:
        if n % multiplier == 0:
            n //= multiplier
        else:
            multiplier += 1
    return multiplier
