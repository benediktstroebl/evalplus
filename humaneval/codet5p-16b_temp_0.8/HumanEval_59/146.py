

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(n, i):
        """Return True if i is a prime factor of n. Assume n > 1 and is not a prime.
        >>> is_prime(86, 2)
        True
        >>> is_prime(86, 3)
        False
        """
        return n % i!= 0
    max_prime_factor = -1
    for i in range(2, n):
        if is_prime(n, i):
            max_prime_factor = i
    return max_prime_factor
