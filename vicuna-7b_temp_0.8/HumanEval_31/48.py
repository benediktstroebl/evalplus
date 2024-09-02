

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
    # This is not the most efficient way to check if a number is prime.
    # This version should be faster than the more efficient ways, but slower than
    # the most efficient version (e.g. trial division).
    
    # Check if the number is prime
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n > 2:
        # Divide the number by 3 to see if it is divisible by 3
        if n % 3 == 0:
            return False
        # Divide the number by 4 to see if it is divisible by 4
        if n % 4 == 0:
            return False
        # Divide the number by 2 to see if it is divisible by 2
        if n % 2 == 0:
            return False
        # Divide the number by 5 to see if it is divisible by 5
        if n % 5 == 0:
            return False
        # If the number is not divisible by 3, 4, 2, or 5, it must be prime
        return True
