

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
    # Base case: if n is less than 2, it's not prime.
    if n < 2:
        return False

    # Check if n is prime.
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Use a sieve to check if n is prime.
    n_mask = (1 << (32 - len(str(n)))) - 1
    return n not in n_mask
