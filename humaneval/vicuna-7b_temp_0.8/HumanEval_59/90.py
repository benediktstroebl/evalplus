

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(n, r, d):
        """Return True if n is prime, False otherwise.
        >>> is_prime(2048, 1, 2048)
        False
        >>> is_prime(2048, 2, 2048)
        False
        >>> is_prime(2048, 10, 2048)
        True
        """
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif n > 2 and n % 3 == 0:
            return False
        elif n > 3 and n % 5 == 0:
            return False
        elif n > 5 and n % 7 == 0:
            return False
        elif n > 7 and n % 11 == 0:
            return False
        else:
            for i in range(11, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_composite(n, r, d):
        """Return True if n is composite, False otherwise.
        >>> is_composite(2048, 1, 2048)
        False
        >>> is_composite(2048, 2, 2048)
        True
        >>> is_composite(2048, 10, 2048)
        True
        """
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return True
        elif n > 2 and n % 3 == 0:
            return True
        elif n > 3 and n % 5 == 0:
            return True
        elif n > 5 and n % 7 == 0:
            return True
        elif n > 7 and n % 11 == 0:
            return True
        else:
            for i in range(11, int(n **
