

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
    # Check if n is 2, 3, 4, or 5, as they are not prime.
    if n == 2 or n == 3 or n == 4 or n == 5:
        return False
    
    # Check if n is divisible by 2, as it is not prime.
    if n % 2 == 0:
        return False
    
    # Check if n is divisible by 3, as it is not prime.
    if n % 3 == 0:
        return False
    
    # Check if n is divisible by 5, as it is not prime.
    if n % 5 == 0:
        return False
    
    # Check if n is divisible by 7, as it is not prime.
    if n % 7 == 0:
        return False
    
    # Check if n is divisible by 11, as it is not prime.
    if n % 11 == 0:
        return False
    
    # If n is not divisible by any of the above numbers, it is prime.
    return True