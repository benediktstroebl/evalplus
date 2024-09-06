

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
    # base case: 0 is not prime
    if n == 0:
        return False
    # base case: 1 is prime
    elif n == 1:
        return True
    # check if n is a prime number
    elif n > 2:
        # check if n has any factors less than or equal to 3
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        if n % 4 == 0:
            return False
        # if none of these checks return True, then n is prime
        return True
