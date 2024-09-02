

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
    # Check for numbers less than 2.
    if n < 2:
        return False
    
    # Check for numbers equal to 2.
    if n == 2:
        return True
    
    # Check for numbers less than the square root of n.
    sqrt_n = int(np.sqrt(n))
    if n < sqrt_n:
        return False
    
    # Check for numbers equal to the square root of n.
    if n == sqrt_n:
        return True
    
    # Check for numbers greater than the square root of n.
    i = 2
    while True:
        # Calculate the number of digits in n.
        digits = len(str(n))
        
        # Calculate the number of factors less than the square root of n.
        factors = (i * i for i in range(1, digits + 1))
        
        # Check if the number of factors equals the square root of n.
        if len(factors) == digits + 1:
            return False
        
        # Check if the number of factors is greater than the square root of n.
        if len(factors) > digits + 1:
            return True
        
        # Increment the number to check.
        i += 2
        
        # Check if the number is a prime number.
        if i > sqrt_n:
            return True
        
        # If the number is not a prime number, the number of factors must be less than the square root of n.
        if i != n:
            return False
    
    # If the number is greater than the square root of n and there are no factors less than the square root of n, the number is prime.
    return True
