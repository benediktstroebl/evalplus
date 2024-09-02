

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
    # 1 is a prime number
    if n == 1:
        return True

    # check if n is prime
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True
