

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
    # Base case: a number is prime if it is 1 or if its last digit is 5 or 7
    if n < 2 or n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    # Iterate over the remaining odd numbers, checking if the number is divisible by any of them
    for i in range(4, int(n**0.5) + 1, 3):
        if n % i == 0:
            return False
    return True
