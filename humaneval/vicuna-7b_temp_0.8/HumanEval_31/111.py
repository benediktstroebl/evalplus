

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
    # if n is less than 2, it is certainly not prime
    if n < 2:
        return False

    # if n is 2, it is the first odd prime and it is certainly prime
    if n == 2:
        return True

    # if n is odd and less than 100, it is not prime
    if n % 2 == 0 or n < 100:
        return False

    # if n is even, it is not prime
    if n % 2 == 0:
        return False

    # try to find the largest power of 2 that divides n
    l = 2
    while l < n // 2:
        if n % l == 0:
            return False
        l += 1

    # if no such power of 2 exists, n is certainly prime
    return True
