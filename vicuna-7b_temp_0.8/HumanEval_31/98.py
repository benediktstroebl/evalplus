

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
    # Special case for 2, which is not a prime number.
    if n == 2:
        return False

    # Special case for 3, which is a prime number.
    elif n == 3:
        return True

    # Check if n is divisible by any number greater than its square root.
    # This will allow us to quickly determine if n is composite.
    if n <= int(sqrt(n)) ** 2:
        return False

    # If n is not divisible by any number greater than its square root, it must
    # be a prime number.
    return True
