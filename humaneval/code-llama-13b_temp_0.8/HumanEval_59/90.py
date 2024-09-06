

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = 0
    for divisor in range(2, n//2 + 1):
        if n % divisor == 0:
            largest = divisor
    return largest

