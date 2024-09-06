

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
    # Check if n is prime by trying to divide n by all the integers from 2 to n-1.
    # If any of these integers evenly divides n, then n is not prime.
    # Otherwise, return True.
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
