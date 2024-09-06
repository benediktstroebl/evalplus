

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            n //= divisor
            return largest_prime_factor(n)
        divisor += 1
    return n


