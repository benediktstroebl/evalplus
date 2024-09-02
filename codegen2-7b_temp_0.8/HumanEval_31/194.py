

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
    """
    We can precompute all of the numbers that are not divisible by 2 or by 1.
    2 is prime.
    1 is not prime.
    """
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
    
