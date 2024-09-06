

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
    # check if n < 2
    if n < 2:
        return False
    
    # check if n is prime
    if n % 2 == 0:
        return False
    
    if n < 3:
        return True
    
    # check if n is divisible by 3
    if n % 3 == 0:
        return False
    
    # keep track of factors until we find a factor
    factors = [n]
    
    # keep track of the last factor we found
    last_factor = 1
    
    # loop through the factors until we find a factor or reach the end of the factors list
    for factor in factors:
        # check if the current factor is less than or equal to the last factor
        if factor <= last_factor:
            return False
        # check if the current factor is greater than the last factor
        else:
            last_factor = factor
    
    # no factors were found, so the number is prime
    return True
