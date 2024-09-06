

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

    """(1) Start off with two things:
    (a) A boolean value `is_prime_so_far` that starts off as True.
    (b) A counter that starts off at 2.

    """
    is_prime_so_far = True
    counter = 2

    """(2) Loop while `is_prime_so_far` is still True.
    """
    while is_prime_so_far:
        """(3) For each number up to the square root of the given number,
        test whether it divides the given number.
        """
        if n % counter == 0:
            is_prime_so_far = False
        counter += 1

    return is_prime_so_far

