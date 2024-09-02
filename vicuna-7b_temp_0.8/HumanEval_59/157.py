

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is prime
    if not n % 2 and not n % 3 and not n % 4 and not n % 5 and not n % 6:
        return n

    # check if n is a prime factor of another number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i

    # n is not prime, so the largest prime factor is n itself
    return n
