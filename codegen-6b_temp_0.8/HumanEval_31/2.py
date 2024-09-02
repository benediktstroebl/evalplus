

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
    # NOTE: The algorithm is still O(n^2) complex; it's not hard to judge
    # whether its complexity is O(n^2) or O(n^1.5) or two times that,
    # depending on the characteristics of the number being checked.
    a = 2
    while a <= (n // 2):
        if n % a == 0:
            return False
        a += 1
    return True
