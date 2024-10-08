

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
    if n in [0, 1]:
        return False
    if n in [2, 3, 5, 7]:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
