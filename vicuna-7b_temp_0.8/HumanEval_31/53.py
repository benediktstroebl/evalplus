

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
    # Use a simple primality test to check if the number is prime
    # If the number is less than 2, it is definitely prime
    # If the number is 2, it is not prime
    # If the number is odd and greater than 2, it is prime
    # If the number is even, it is not prime
    # If the number has more than 3 digits, it is not prime
    if n < 2 or n == 2 or n % 2 != 0 or len(str(n)) > 3:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
