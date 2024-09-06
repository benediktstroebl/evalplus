

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
    # n is less than 2
    if n < 2:
        return False
    # n is exactly 2
    if n == 2:
        return True
    # if n is divisible by 2
    if n % 2 == 0:
        return False
    #Check if n is divisible by any number between 3 and int(n/2)
    for i in range(3, int(n/2)):
        if n % i == 0:
            return False
    return True
