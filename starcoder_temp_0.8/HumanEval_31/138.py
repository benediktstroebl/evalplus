

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
    # initialize a counter to 0
    k = 0
    # create a loop from 1 to the given number
    for i in range(1, n+1):
        # increase k if the remainder of n/i is zero
        if n % i == 0:
            k += 1
            # if k > 2, then n is not a prime number
            if k > 2:
                return False
    # if the given number is prime, then return True
    return True
