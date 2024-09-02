

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
    # first, check if the number is prime
    if n > 1:
        # try to divide it by the prime number 2
        if n % 2 == 0:
            return False
        # try to divide it by the prime number 3
        if n % 3 == 0:
            return False
        # try to divide it by the prime number 4
        if n % 4 == 0:
            return False
        # try to divide it by the prime number 5
        if n % 5 == 0:
            return False
        # try to divide it by the prime number 6
        if n % 6 == 0:
            return False
        # repeat this process for all the prime numbers
        # up to the square root of the input number
        for i in range(int(np.sqrt(n))):
            if n % i == 0:
                return False
        # if we reach the end of this loop without finding any factors
        # then the number must be prime
        return True
    # if the number is 0 or less than 1, it is not prime
    return False
