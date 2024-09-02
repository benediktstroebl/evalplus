

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
    # if n is 2 then it's prime
    if n == 2:
        return True
    # if n is not even then it's not prime
    if n % 2 == 0:
        return False
    # if n is less than 0 then it's not prime
    if n < 0:
        return False

    # if there's no divisor in range of 3 to n-1, then n is prime
    for i in range(3, n):
        if n % i == 0:
            return False

    return True
