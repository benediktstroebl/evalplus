

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
    # Check if n is prime
    # Based on the Sieve of Eratosthenes algorithm
    if n < 3:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n > 3 and n % 5 == 0:
        return False
    elif n > 5 and n % 7 == 0:
        return False
    elif n > 7 and n % 11 == 0:
        return False
    else:
        # Check if n is divisible by any of the small primes up to sqrt(n)
        for i in range(3, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
