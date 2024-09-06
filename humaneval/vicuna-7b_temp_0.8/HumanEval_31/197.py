

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
    # Base case: if n is less than 2, it is certainly not prime
    if n < 2:
        return False
    
    # If n is 2, it is certainly prime
    if n == 2:
        return True
    
    # If n is odd, it is certainly prime
    if n % 2 == 1:
        return True
    
    # If n is even, it is not prime
    if n % 2 == 0:
        return False
    
    # Iterate over the range 2 to (n-1)/2, inclusive, and check if n is divisible by any of those numbers.
    # If it is not, then n must be prime.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
