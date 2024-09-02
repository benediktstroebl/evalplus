

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
    # Code skeleton from example solution to Code Wars
    # Base case
    if n == 1:
        return False
    # Checks the divisor with all divisors from 2 up to n, and returns false
    # if smallest divisor is a factor of n; otherwise returns true
    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

