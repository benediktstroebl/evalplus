

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for i in range(3, n+1, 2):
        if i > n/i:
            break
        while n % i == 0:
            n = n // i
    return n

