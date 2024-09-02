

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is prime
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0:
            return i
    return 6
