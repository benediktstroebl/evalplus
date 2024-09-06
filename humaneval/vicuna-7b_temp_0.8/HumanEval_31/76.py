

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
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n > 5 and n % 6 == 0:
        return False
    if n > 10 and n % 7 == 0:
        return False
    if n > 100 and n % 8 == 0:
        return False
    if n > 1000 and n % 9 == 0:
        return False
    if n > 10000 and n % 10 == 0:
        return False
    if n > 100000 and n % 11 == 0:
        return False
    return True
