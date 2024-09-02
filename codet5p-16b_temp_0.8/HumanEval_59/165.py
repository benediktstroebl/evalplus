

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        return None
    result = n
    n = n - 1
    while n > 1:
        result = n
        n = n - 1
        if n == 1:
            return result
        if is_prime(n):
            return n
    return result
