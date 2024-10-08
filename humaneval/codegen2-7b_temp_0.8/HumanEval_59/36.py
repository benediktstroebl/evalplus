

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = 2
    n = abs(n)
    while n % prime_factor!= 0:
        prime_factor += 1
    return prime_factor

