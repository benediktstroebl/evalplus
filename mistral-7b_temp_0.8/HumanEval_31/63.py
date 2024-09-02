

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
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True

