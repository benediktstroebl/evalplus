

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
    # Check if n is prime by checking if it's divisible by any number less than its square root.
    # This is an efficient algorithm that has a time complexity of O(sqrt(n)).
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True
