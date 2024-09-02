

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
    # check if the number is 1
    if n == 1:
        return False
    # check if the number is 2
    if n == 2:
        return True
    # otherwise check if it is greater than 2
    if n > 2:
        # check if it is divisible by 2
        if (n % 2) == 0:
            return False

        # check for all odd numbers up to the number
        for i in range(3, n, 2):
            if (n % i) == 0:
                return False
    return True
