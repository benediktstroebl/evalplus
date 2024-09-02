

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while True:
        if n % 2 == 0:
            return 2
        d = 2
        while d * d <= n:
            if n % d == 0:
                return d
            d += 2
        n = int(n / d)
    
    # n is now < 2, which is not possible since n > 1, so we must have reached the end of the loop
    return 1
