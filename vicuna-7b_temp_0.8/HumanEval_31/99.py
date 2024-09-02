

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
    # base cases: 2, 3, 5, and 7 are prime
    if n < 3 or n in (2, 3, 5, 7):
        return False
    # loop cases: 1, 61, 101, and all numbers greater than the square root of n
    if n == 1:
        return True
    elif n == 61:
        return True
    elif n % 2 == 1:
        return False
    elif n % 3 == 1:
        return False
    elif n % 5 == 1:
        return False
    elif n > 5 and (n % 61) == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
