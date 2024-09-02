

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
    # Base case: check if n is 2, which is a special case.
    if n == 2:
        return True

    # If n is not 2, check if it is odd. If it is odd, we know it is not
    # divisible by any integer except 1, so it must be prime. If it is even,
    # we can't say it is prime or not.
    if n % 2 == 0:
        return False

    # Now we need to check if n is divisible by any integer between 3 and
    # sqrt(n) (both inclusive). If it is, it must be composite, so we can
    # return False.
    if n % (3, 6) != 0:
        return False

    # If n is still not divisible by any number, we can say it is prime.
    return True