

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    divisor = 3
    while divisor <= n // divisor:
        if n % divisor == 0:
            return divisor
        divisor += 2
    return n // 2
