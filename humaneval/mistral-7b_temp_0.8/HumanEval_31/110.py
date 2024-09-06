

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
    # Your code goes here

    # If n is less than 2 or if n is even, it is not a prime number
    if n < 2 or n % 2 == 0:
        return False

    # Iterate through all numbers between 3 and n/2
    for i in range(3, int(n ** 0.5) + 1, 2):
        # If n is divisible by i, it is not a prime number
        if n % i == 0:
            return False

    # If we reach this point, n is a prime number
    return True
