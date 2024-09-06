

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
    # if n < 2, it's not prime
    if n < 2:
        return False
    
    # if n is 2, it's prime
    if n == 2:
        return True
    
    # if n is odd, it's prime
    if n % 2 == 1:
        return True
    
    # check if n is divisible by any integer between 3 and n/2, except n/2
    for i in range(3, int(n/2)+1, 2):
        if n % i == 0:
            return False
    
    # if none of the above conditions are met, the number is prime
    return True
