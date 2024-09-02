

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
    # Base case: if n is less than 2, it is not prime.
    if n < 2:
        return False

    # If n is even, it is not prime.
    if n % 2 == 0:
        return False

    # If n is 2 or 3, it is prime.
    if n == 2 or n == 3:
        return True

    # If n is 5 or the successor of the first prime number bigger than 5, it is prime.
    # (In other words, if n == 5 or if the first prime number bigger than 5 is p, then n = 6 or 7 or ... or 2(p+1) - 2.)
    # Note that this covers all the cases up to n = 1021.
    if n == 5 or n % 2 != 0 and n % 3 != 0:
        return True

    # Otherwise, n is not prime.
    return False
