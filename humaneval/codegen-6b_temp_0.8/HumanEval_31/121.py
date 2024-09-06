

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
    #Check if n is a positive integer
    assert type(n) == int and n > 0, 'n must be a positive integer'

    #Check n is prime
    if n == 1:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False

    #Try to divide n by 2 from 2 to n
    for i in range(3, n, 2):
        if not n % i:
            return False
        return True
