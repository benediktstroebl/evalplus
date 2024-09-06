

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
    # Base case: A number is prime if it is less than 2
    if n < 2:
        return False
    # An odd number greater than 2 is prime if all the numbers from 2 to n
    # divide into it with a remainder
    elif n % 2 != 0:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    else:
        return False

