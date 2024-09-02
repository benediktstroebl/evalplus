

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def prime_factor(n: int):
        """Return a list of prime factors of n.
        >>> prime_factor(3)
        [3]
        >>> prime_factor(6)
        [2, 3]
        >>> prime_factor(12)
        [2, 2, 3]
        >>> prime_factor(100)
        [2, 2, 5, 5]
        >>> prime_factor(512)
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
