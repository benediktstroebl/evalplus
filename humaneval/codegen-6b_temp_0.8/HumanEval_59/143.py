

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n //= 2
    # n is odd at this point and can only be divided by odd primes
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # only odd primes
        while n % i == 0:
            n //= i
    return n

