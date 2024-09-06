

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
    # Special case: 2 is a prime, but we handle it separately for efficiency.
    if n == 2:
        return False
    # Special case: 3 is a prime, but we handle it separately for efficiency.
    elif n == 3:
        return True
    # Handle the rest of the numbers in this loop.
    else:
        # Check the number to see if it's divisible by 2.
        if n % 2 == 0:
            return False
        # Check the number to see if it's divisible by 3.
        if n % 3 == 0:
            return False
        # Check the number to see if it's divisible by 5.
        if n % 5 == 0:
            return False
        # Check the number to see if it's divisible by 7.
        if n % 7 == 0:
            return False
        # Check the number to see if it's divisible by 11.
        if n % 11 == 0:
            return False
        # Check the number to see if it's divisible by 13.
        if n % 13 == 0:
            return False
        # Check the number to see if it's divisible by 17.
        if n % 17 == 0:
            return False
        # Check the number to see if it's divisible by 19.
        if n % 19 == 0:
            return False
        # Check the number to see if it's divisible by 23.
        if n % 23 == 0:
            return False
        # Check the number to see if it's divisible by 29.
        if n % 29 == 0:
            return False
        # Check the number to see if it's divisible by 31.
        if n % 31 == 0:
            return False
        # Check the number to see if it's divisible by 37.
        if n % 37 == 0:
            return False
        # Check the number to see if it's divisible by 41.
