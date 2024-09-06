

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

    # handle small numbers
    if n <= 3:
        return n > 1

    # even number
    if n % 2 == 0:
        return False

    # odd number
    for i in range(3, int(n**.5) + 1, 2):
        if n % i == 0:
            return False

    return True

