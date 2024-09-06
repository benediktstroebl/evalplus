

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
    # Handle the base cases of 0 and 1 by returning False
    if n < 2:
        return False
    # Handle the case of 2, which is not prime
    if n == 2:
        return False
    # Check if n is even, if so it is not prime
    if n % 2 == 0:
        return False
    # Check if n is divisible by any number less than its square root
    # by repeatedly dividing n by the square root of n
    # until the quotient is not a factor of n
    sqrt = math.sqrt(n)
    while True:
        if n % sqrt == 0:
            return False
        n = n // sqrt
    # At this point, n is not divisible by any number less than its square root
    # Therefore, it is prime
    return True