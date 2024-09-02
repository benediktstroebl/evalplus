

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
    if n < 1:
        return False
    elif n in (2,3,5,7,11,13):
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for d in range(17, n // 2, 17):
            if n % d == 0:
                return False
        return True
