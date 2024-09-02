

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
    # Check if n is a prime
    if n > 2:
        # Loop through the primes less than n
        for p in range(2, int(n ** 0.5) + 1):
            # Check if n is divisible by p
            if n % p == 0:
                return False
        return True
    else:
        return False
