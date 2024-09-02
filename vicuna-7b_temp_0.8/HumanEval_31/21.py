

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
    # Special case: 2 is not considered prime
    if n == 2:
        return False

    # Special case: 3 is a prime, but 4 is not considered prime
    elif n == 3:
        return True

    # Test if n is divisible by any integer between 2 and sqrt(n)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    # If n is not divisible by any integer between 2 and sqrt(n), it is prime
    return True