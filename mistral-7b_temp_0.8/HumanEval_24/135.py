

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def is_divisor(n: int, m: int) -> bool:
        """ Check if n is a divisor of m
        >>> is_divisor(10, 20)
        True
        >>> is_divisor(10, 11)
        False
        """
        return n % m == 0

    divisor = 1
    while is_divisor(divisor, n):
        divisor += 1
    return divisor - 1
