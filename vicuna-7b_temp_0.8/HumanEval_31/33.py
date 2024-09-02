

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
    if n > 2:
        # If n is odd, check if it is prime by dividing it by 3
        if n % 3 == 0:
            return False
        # If n is even, check if it is prime by dividing it by 2 and 3
        if n % 2 == 0:
            return is_prime(n // 2) and is_prime(n // 3)
        # If n is greater than 3, it is prime
        else:
            return True
    else:
        return True
