

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError("Input must be greater than 1")

    for i in range(2, n):
        while n % i == 0:
            n = n / i

    return n

