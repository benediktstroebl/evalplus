

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
    # checking numbers from 2 to n-1
    for i in range(2, n):
        # checking if number is a multiple of any of the previous numbers
        if n % i == 0:
            return False
    return True

