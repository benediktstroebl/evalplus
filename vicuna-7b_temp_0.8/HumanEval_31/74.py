

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
    # Handle the base case of 2, which is always prime.
    if n == 2:
        return True

    # Handle the base case of 3, which is always prime except for 3 itself.
    if n == 3:
        return False

    # Check for composite numbers.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    # If we reach this point, the number is prime.
    return True
