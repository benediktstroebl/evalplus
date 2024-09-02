

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
    # The list of known composite numbers
    composite_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 60, 100, 120, 10000]
    
    # Check if n is divisible by any number in the list of composite numbers
    for composite in composite_numbers:
        if n % composite == 0:
            return False
            
    # Check if n is divisible by 1 or 2
    if n == 1 or n == 2:
        return False
    
    # n is not divisible by any number in the list of composite numbers,
    # and n is not 1 or 2, so it must be prime
    return True
    