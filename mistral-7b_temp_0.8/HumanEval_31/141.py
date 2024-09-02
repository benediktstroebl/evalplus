

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
    # 0 and 1 are not prime
    if n in [0,1]:
        return False
    # 2 is a prime number
    if n == 2:
        return True
    # odd number
    if n % 2 != 0:
        # checking odd number, starting from 3
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        # all odd numbers below the square root of n are checked
        return True
    # even number
    else:
        # checking even number, starting from 2
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        # all even numbers below the square root of n are checked
        return True
