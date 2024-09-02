

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    # the only divisors of a prime are 1 and the number itself
    # so we start with n + 1 and check whether we can divide n without finding a
    # factor. If we find a factor, we return False. If we can't find a factor,
    # then we return True
    for possible_factor in range(2, n):
        if n % possible_factor == 0:
            return False
    return True

