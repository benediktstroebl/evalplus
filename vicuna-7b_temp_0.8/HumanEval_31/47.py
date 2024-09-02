

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
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n < 11:
        return True
    elif n % 3 == 0:
        return False
    elif n < 1000000:
        # Use sieve of Eratosthenes to check if n is prime
        return (n > (int(sqrt(n)) + 1) and n % (int(sqrt(n)) + 1) == 0)
    else:
        # Use trial division to check if n is prime
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
