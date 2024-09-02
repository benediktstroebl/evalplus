

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
    # base case: if n <= 2, it is not prime
    if n <= 2:
        return False
    
    # if n is 3, it is prime
    if n == 3:
        return True
    
    # try to find a prime factor of n (if there is one)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # if no prime factor was found, then n must be prime
    return True