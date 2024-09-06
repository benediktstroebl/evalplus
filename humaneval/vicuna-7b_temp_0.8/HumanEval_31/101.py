

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
        # Check if n is prime
        if n > 2:
            # Check if n is divisible by 2
            if n % 2 == 0:
                return False
        # Check if n is divisible by 3
        if n > 3:
            # Check if n is divisible by 3
            if n % 3 == 0:
                return False
        # Check if n is divisible by 4
        if n > 4:
            # Check if n is divisible by 4
            if n % 4 == 0:
                return False
        # Check if n is divisible by 5
        if n > 5:
            # Check if n is divisible by 5
            if n % 5 == 0:
                return False
        # Check if n is divisible by 6
        if n > 6:
            # Check if n is divisible by 6
            if n % 6 == 0:
                return False
        # Check if n is divisible by 7
        if n > 7:
            # Check if n is divisible by 7
            if n % 7 == 0:
                return False
        # Check if n is divisible by 8
        if n > 8:
            # Check if n is divisible by 8
            if n % 8 == 0:
                return False
        # Check if n is divisible by 9
        if n > 9:
            # Check if n is divisible by 9
            if n % 9 == 0:
                return False
        # Check if n is divisible by 10
        if n > 10:
            # Check if n is divisible by 10
            if n % 10 == 0:
                return False
        # Check if n is divisible by 11
        if n > 11:
            # Check if n is divisible by 11
            if n % 11 == 0:
                return False
    return True
