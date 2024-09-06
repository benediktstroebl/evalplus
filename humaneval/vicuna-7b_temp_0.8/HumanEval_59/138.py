

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 3:
        return 2
    if n % 2 == 0:
        return n/2
    while True:
        if n % 3 == 0:
            n = 3*n/5
        elif n % 5 == 0:
            n = 5*n/5
        elif n % 7 == 0:
            n = 7*n/7
        elif n % 11 == 0:
            n = 11*n/11
        else:
            break
    return n
