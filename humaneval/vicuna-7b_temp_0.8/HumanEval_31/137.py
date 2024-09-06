

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
    # If the number is 2, it's not prime
    if n == 2:
        return False
    # If the number is not a prime number, it's not prime
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0:
        return False
    # If the number is not a prime number, it's not prime
    for i in range(5, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
