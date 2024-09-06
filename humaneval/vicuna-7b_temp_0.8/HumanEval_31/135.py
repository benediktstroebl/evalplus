

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
    # 6 is a special case.
    if n == 6:
        return False

    # 7 is also a special case.
    if n == 7:
        return True

    # If n is not a prime number, it can't be greater than the square root of n.
    if n >= (int(sqrt(n)) + 1):
        return False

    # If n is not prime, it can't be less than the square root of n plus 2.
    if n < (int(sqrt(n)) - 1):
        return False

    # Check the last two digits of n.
    # n should have at least 2 digits because n >= 2.
    last_two_digits = str(n)[-2:].zfill(2)
    if last_two_digits.isdigit(2) and last_two_digits.isdigit(1):
        return False

    # If we got this far, n is prime.
    return True