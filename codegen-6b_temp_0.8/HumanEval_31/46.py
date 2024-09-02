

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
    # hint: whether this is the prime number is as simple as multiplying the number by itself
    # and checking if it's divisible by any number but 1 and itself

    "*** YOUR CODE HERE ***"
    if n < 2:
        return False
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    m = 3
    while m <= n**0.5:
        if n % m == 0:
            return False
        m += 2
    return True
