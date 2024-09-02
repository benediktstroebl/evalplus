

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
    # Your code here
    #if n is 2 or 1, return True
    if n == 2:
        return True
    if n == 1:
        return False
    #otherwise check if n is divisible by any number between 2 and n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
