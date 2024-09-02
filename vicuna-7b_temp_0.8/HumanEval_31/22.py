

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
    # This function uses a simple trial division method to check if a number is prime.
    # It is not very efficient, but it should work for smallish numbers.
    #
    # The basic idea is to check if the number has any factors smaller than its square root.
    # If it does not, then it is prime.
    #
    # This function assumes that the number is positive.

    # Check if the number is positive
    if n < 0:
        raise ValueError("A positive number is required.")

    # Check if the number is prime
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    for x in range(4, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
