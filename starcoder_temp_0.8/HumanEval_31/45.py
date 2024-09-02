

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
    # see https://en.wikipedia.org/wiki/Primality_test
    if n == 1:
        return False

    if n == 2:
        return True

    for j in range(2,n-1):
        if n % j == 0:
            return False

    return True
