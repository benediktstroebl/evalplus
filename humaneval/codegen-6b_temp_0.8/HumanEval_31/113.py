

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
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    elif n % 3 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0 or n % 5 == 0:
        return False
    while n % 6 != 1 and n % 6 != 5:
        n = n - 1
        if n % 6 == 1 or n % 6 == 5:
            return False
    return True
