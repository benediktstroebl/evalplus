

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
    # if n is prime, return true
    if n > 1:
        return n == (1)
    # if n is not prime, check if it's a factor of a prime n
    else:
        # loop over all prime numbers
        for p in primes:
            # if n is a factor of prime n, return false
            if n % p == 0:
                return False
        # if n is not a factor of any prime, it's prime
        return True