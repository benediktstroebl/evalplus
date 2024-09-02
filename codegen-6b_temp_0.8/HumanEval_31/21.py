

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
    assert n > 0, "n must be a positive integer."
    assert type(n) is int, "n must be an integer."
    i = 2
    while n > 1:
        if n % i == 0:
            return False
        i += 1
    return True
