

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    while n % 2 == 0:
        n //= 2
    divisor = 3
    while n > 1 and n % divisor != 0:
        divisor += 2
    if n > 1:
        return largest_prime_factor(n)
    return divisor
