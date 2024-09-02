

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
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n < 11:
        return True
    elif n % 3 == 0:
        return False
    else:
        "all primes > 3 are of the form 6k - 1 or 6k + 1"
        return all(n % i != 0 for i in range(5, int(math.sqrt(n)) + 1, 6))
