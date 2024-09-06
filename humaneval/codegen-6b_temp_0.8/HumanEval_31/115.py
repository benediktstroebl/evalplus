

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
    # If n == 1, 0, or negative, return false
    if n < 2:
        return False
    # If n is even, return false
    if n%2==0:
        return False
    # If n is 3, or greater, give the answer true
    if n > 3:
        return True
    # Start with the first prime of n
    a = 3
    # Try to divide n and 2 to find the prime factors
    while n % a != 0:
        a += 2
    # If a is not prime, return false
    if a != 2 and a != 3 and a != 5:
        return False
    # If n is divisible by a, it is not prime
    if n % a == 0:
        return False
    # else, we know that n is prime, and we cannot verify further
    # as a, b, c cannot all be primes
    return True
