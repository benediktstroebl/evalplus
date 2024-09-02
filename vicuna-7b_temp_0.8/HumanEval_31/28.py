

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
    # Base case: if n is less than 2, it's not prime
    if n < 2:
        return False

    # If n is 2, it's prime
    if n == 2:
        return True

    # If n is odd, it's prime
    if n % 2 != 0:
        return True

    # Iterate over the range 2 to n-1 and check if the number is divisible by any of them
    for i in range(2, n-1):
        if not (n % i):
            return False

    # If we reach this point, the number is prime
    return True
