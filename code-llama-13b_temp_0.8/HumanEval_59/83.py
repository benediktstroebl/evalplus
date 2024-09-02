

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 0
    divisor = 2
    while n > 1:
        while n % divisor != 0:
            divisor += 1
        n = n // divisor
        if divisor > largest_prime:
            largest_prime = divisor
        divisor += 1
    return largest_prime

