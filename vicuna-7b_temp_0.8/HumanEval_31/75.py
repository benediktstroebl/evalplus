

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
    # Set the number to be tested and the counter to 2
    n = int(n)
    counter = 2
    
    # Loop until the counter is greater than the square root of n
    while counter <= sqrt(n):
        # If the counter is even, the number is not prime
        if counter % 2 == 0:
            return False
        
        # If the counter is odd, check if it is divisible by any number less than n
        if counter % 2 == 1:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
        else:
            # If the counter is odd and greater than 1, check if it is divisible by n
            if counter > 1:
                if n % counter == 0:
                    return False
    
    # If the counter has not found any divisor, the number is prime
    return True
