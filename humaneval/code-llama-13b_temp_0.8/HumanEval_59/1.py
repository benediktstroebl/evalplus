

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    prime_factor = 1
    for i in range(2, n//2):
        if n % i == 0:
            prime_factor = i
    return prime_factor

