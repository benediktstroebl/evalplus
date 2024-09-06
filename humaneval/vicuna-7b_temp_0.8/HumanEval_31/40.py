

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
    # 1 is always prime, so we can skip it
    if n == 2:
        return True
    
    # check if n is prime by using trial division
    # 67 is the largest n for which n % 67 is not greater than 59
    # 67 is also the largest n for which the loop below will terminate
    for i in range(67, len(str(n))):
        if n % i == 0:
            return False
    return True
