

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # assume n is prime
    pf = n - 1
    while pf % 2 == 0:
        pf = pf // 2
    # Search for a prime factor
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            pf = n // i
    return pf

