

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
    if n == 1:
        return False
    elif n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    elif n > 2 and n % 3 == 0:
        return False
    else:
        return all([n % i for i in range(n - 1, 1, -2)])
