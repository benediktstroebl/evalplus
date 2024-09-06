

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
    # Check if the given number is less than 2.
    if n <= 1:
        return False
    # Check if the given number is equal to 2.
    elif n == 2:
        return True
    # Check if the given number is not even.
    elif n % 2 == 0:
        return False
    # Check if the given number is not divisible by 3 or 5.
    elif n % 3 == 0 or n % 5 == 0:
        return False
    # Check if the given number is not divisible by 7 or 11.
    elif n % 7 == 0 or n % 11 == 0:
        return False
    # Check if the given number is not divisible by 13 or 17.
    elif n % 13 == 0 or n % 17 == 0:
        return False
    # Check if the given number is not divisible by 19 or 23.
    elif n % 19 == 0 or n % 23 == 0:
        return False
