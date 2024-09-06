

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
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    if n % 11 == 0 or n % 13 == 0 or n % 17 == 0 or n % 19 == 0:
        return False
    for i in range(23, n, 2):
        if n % i == 0:
            return False
    return True

