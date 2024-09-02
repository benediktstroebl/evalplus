

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
    # Check if the number is evenly divisible by each number from 2 up to but not including the square root of n
    # If the number is evenly divisible by any of the numbers from 2 up to but not including the square root,
    # it is not prime
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        # Get the square root of n + 1
        a = int((n + 1) ** 0.5)
        # Iterate through 2 to the square root of n + 1
        for i in range(2, a + 1):
            # If there is a remainder, the number is not prime
            if n % i == 0:
                return False
    return True
    