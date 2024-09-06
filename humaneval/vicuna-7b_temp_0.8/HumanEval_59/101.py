

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
    while True:
        p = 1000000007
        i = 0
        while p % i == 0:
            i += 1
        if i > 0:
            p = p - i
        if n > p:
            return p
        n //= 2
