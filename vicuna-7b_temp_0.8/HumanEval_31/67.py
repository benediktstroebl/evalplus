

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
    # Check if n is prime
    if (n > 1):
        # Loop through the numbers 2 to n-1
        for i in range(2, int(n**0.5) + 1):
            # If n is divisible by i, it is not prime
            if not (n % i == 0):
                return False
        # If n is not divisible by any number between 2 and its square root, it is prime
        return True
    # Special case for n = 1
    return not (n > 1)
