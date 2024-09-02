

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
    # start at 2, a non-prime number
    for i in range(2, n):
        # if it divides evenly, then it is not prime
        if n % i == 0:
            return False
    # if we get this far, n must be prime
    return True

