

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
    # If number is even, it cannot be prime
    if n == 2 or n == 1:
        return True
    elif n%2 == 0:
        return False
    else:
        # if any number larger than n/2 can be evenly divided by n, then the number is not prime
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

