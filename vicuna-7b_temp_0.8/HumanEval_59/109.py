

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 1
    while True:
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        d = sqrt(n)
        if d % 2 == 0:
            return d
        n = int(n/d)
        if n == 1:
            return 1
        if n > 1000000:
            return n

a = [largest_prime_factor(i) for i in range(1, 101)]
