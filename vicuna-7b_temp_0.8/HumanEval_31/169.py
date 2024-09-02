

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
    # check if n is less than 2, then it is prime
    if n < 2:
        return True
    # check if n is 2, then it is not prime
    elif n == 2:
        return False
    # check if n is 3, then it is prime
    elif n == 3:
        return True
    # check if n is odd and greater than 3, then it is prime
    else:
        return n > 3 and (n % 2) == 1 and (n % 3) == 0 and (n > 3)