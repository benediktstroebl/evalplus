

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
    # Handle the special case of 2, which is always prime
    if n == 2:
        return True
    
    # Handle the special case of 3, which is not always prime
    if n == 3:
        return True
    
    # Check if n is divisible by any number between 2 and sqrt(n)
    if n % (2, sqrt(n)) == 0:
        return False
    
    # Loop through the prime numbers and check if n is divisible by any of them
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    
    return True