

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
    # the trivial case
    if n == 1:
        return False
    # if n is even, it's not prime
    elif n % 2 == 0:
        return False
    # if n is either 2 or 3, it's prime
    elif n in [2, 3]:
        return True
    # the only even number greater than 2 is 4
    elif n > 4:
        if n % 2 == 0:
            return False
    # loop through all numbers less than n**0.5
    for i in range(3, int(n ** 0.5) + 1, 2):
        # if the number is divisible by i, n is not prime
        if n % i == 0:
            return False
    # if we get here, then n is prime
    return True
