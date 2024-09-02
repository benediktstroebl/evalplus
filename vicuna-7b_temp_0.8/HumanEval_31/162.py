

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
    # Check if the number is prime
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n <= 3:
        return True
    elif n % 3 == 0:
        return False
    elif n <= 7:
        return True
    elif n % 7 == 0:
        return False
    elif n <= 19:
        return True
    elif n % 19 == 0:
        return False
    elif n <= 49:
        return True
    elif n % 49 == 0:
        return False
    elif n <= 97:
        return True
    elif n % 97 == 0:
        return False
    elif n <= 199:
        return True
    elif n % 199 == 0:
        return False
    elif n <= 399:
        return True
    elif n % 399 == 0:
        return False
    elif n <= 799:
        return True
    elif n % 799 == 0:
        return False
    elif n <= 999:
        return True
    elif n % 999 == 0:
        return False
    elif n <= 1999:
        return True
    elif n % 1999 == 0:
        return False
    else:
        return True
