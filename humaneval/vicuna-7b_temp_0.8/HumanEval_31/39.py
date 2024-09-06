

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
    if n > 1:
        # Check if n is divisible by 2
        if n % 2 == 0:
            return False
        # Check if n is divisible by 3
        if n % 3 == 0:
            return False
        # Check if n is divisible by 4
        if n % 4 == 0:
            return False
        # Check if n is divisible by 5
        if n % 5 == 0:
            return False
        # Repeat the above process for larger numbers
        for i in range(6, int(np.log2(n)) + 1, 2):
            if n % (i + 2) == 0:
                return False
        # If all checks pass, return True
        return True
    else:
        return False
