

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
    # Base cases: 1 and the number itself are always prime
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    # Recursive case for odd numbers greater than 3
    if n > 3:
        return (n > 1) or (n % 2 == 0) or (is_prime(n - 1))

    # Recursive case for even numbers less than 100
    if n < 100:
        return True

    # If the number is not prime, return false
    return False
