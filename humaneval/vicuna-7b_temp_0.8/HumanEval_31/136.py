

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
    # Check if n is prime
    if n > 1:
        # Check if n is even
        if n % 2 == 0:
            return False
        # Check if n is odd
        else:
            # Check if n is divisible by 3
            if n % 3 == 0:
                return False
            # Check if n is divisible by 5
            if n % 5 == 0:
                return False
            # Check if n is divisible by 7
            if n % 7 == 0:
                return False
    return True
