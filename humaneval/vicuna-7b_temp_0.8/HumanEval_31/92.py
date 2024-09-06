

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
    # Try to see if n is divisible by any of the known prime numbers
    # from 2 to n-1
    if n > 2 and not n % 2:
        return False
    if not n % 3:
        return False
    if not n % 5:
        return False
    if not n % 7:
        return False
    if not n % 11:
        return False
    
    # If n is divisible by any of the above numbers, it is not prime
    return False
