

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
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n < 3:
        return True
    elif n % 3 == 0:
        return False
    elif n < 11:
        return True
    elif n % 11 == 0:
        return False
    elif n < 10000:
        if n % 13 == 0:
            return False
        elif n % 17 == 0:
            return False
        elif n % 19 == 0:
            return False
        elif n % 23 == 0:
            return False
        elif n % 29 == 0:
            return False
        else:
            return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
