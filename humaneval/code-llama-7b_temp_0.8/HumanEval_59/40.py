

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Special cases
    if n % 2 == 0:
        return 2

    # Keep only odd numbers in the loop
    divisor = 3
    while divisor ** 2 <= n:
        while n % divisor == 0:
            n = n // divisor
        divisor += 2

    return n

