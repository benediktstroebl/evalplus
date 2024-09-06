

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
    """
    If the number is even and not 2, return False
    """
    if n%2 == 0:
        if n == 2:
            return True
        else:
            return False
    """
    If the number is odd, divide it by every number from 2 to itself
    and see if it is divisible by any number in that range.
    If it is divisible by any number in that range, return False
    """
    for x in range(2, n+1):
        if n%x == 0:
            return False
    return True

