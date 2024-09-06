

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
    "*** YOUR CODE HERE ***"
    # if the number is 1 or 0, it is not prime.
    if n == 1 or n == 0:
        return False
    # if the number is 2, it is prime
    if n == 2:
        return True
    # if the number is even, it is not prime
    if n % 2 == 0:
        return False
    # otherwise, check if it is divisible by any number from 3 to n-1.
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

