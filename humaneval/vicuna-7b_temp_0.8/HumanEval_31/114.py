

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
    # base cases
    if n == 2:
        return True
    elif n == 3:
        return True
    elif n in (2, 3):
        return True
    elif n < 5:
        return False
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n > 5:
        return True
    # recursive case
    else:
        for i in range(6, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
