

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
    # If the input number is not a positive integer, return false
    if n <= 0:
        return False
    
    # Check if the number is prime by testing divisibility of its square.
    # If n^2 is divisible by any number between 2 and sqrt(n), then n is not prime.
    if n > 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    
    # If no divisor has been found, return true
    return True
