

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    p = 2
    while True:
        # If n is prime, then p is the answer.
        if n == p:
            return n

        if n % p == 0:
            # p is a divisor of n,
            n = n // p
        else:
            p += 1

