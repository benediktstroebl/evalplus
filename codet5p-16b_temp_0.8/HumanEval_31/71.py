

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

    if n == 2:
        return True
    if n == 3:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    if n % 13 == 0:
        return False
    if n % 17 == 0:
        return False
    if n % 19 == 0:
        return False
    if n % 23 == 0:
        return False
    if n % 29 == 0:
        return False
    if n % 31 == 0:
        return False
    if n % 37 == 0:
        return False
    if n % 41 == 0:
        return False
    if n % 43 == 0:
        return False
    if n % 47 == 0:
        return False
    if n % 53 == 0:
        return False
    if n % 59 == 0:
        return False
    if
