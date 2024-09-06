

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        raise ValueError("n should be greater than 1.")
    if n == 2 or n == 3:
        return n
    for i in range(2, n):
        if n % i == 0:
            n //= i
    return n

