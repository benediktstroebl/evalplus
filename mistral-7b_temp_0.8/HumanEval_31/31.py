

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
    # you have to check for even numbers first
    # if number is even, return False
    # for numbers between 2 and n-1
    # if the number is evenly divisible by any
    # of those numbers, return False
    # if not, return True
    if n == 2 or n % 2 != 0:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
    return True

