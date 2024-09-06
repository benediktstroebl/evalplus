

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
    # if n is less than 1
    if n < 1:
        return False
    # loop over possible divisors
    for i in range(2, n):
        # return False if n is divisible by any number between 2 and n-1
        if n % i == 0:
            return False
    # return True if no divisor is found
    return True
