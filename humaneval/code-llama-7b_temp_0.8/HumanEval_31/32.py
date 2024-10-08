

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
    # Is a number divisible by 2?
    if n%2==0:
        return False
    # Does the number have any other factors?
    for i in range(3,n):
        if n%i==0:
            return False
    return True

