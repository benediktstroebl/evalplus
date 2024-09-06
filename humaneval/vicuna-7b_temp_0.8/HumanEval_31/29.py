

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
    # Loop through the range 2 to the square root of n,
    # and for each number check if it is equal to n.
    # If it is, then n is not prime, so return False.
    # If it is not, then continue with the next number.
    # If all the numbers in the range are not equal to n,
    # then return True.
    #
    # Note that this method is highly inefficient, as it
    # requires checking each number from 2 to sqrt(n) twice.
    # A better method would be to use a sieve or a more efficient
    # primality test.
    for i in range(2, int(n ** 0.5) + 1):
        if n == i:
            return False
    return True
