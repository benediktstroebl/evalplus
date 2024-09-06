

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
    prime = True;

    # check if n is divisible by 2 or 3 first
    if n % 2 == 0 or n % 3 == 0:
        prime = False
    
    # check if n is divisible by values i that are not divisible by 2 or 3 first
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            prime = False

    return prime
