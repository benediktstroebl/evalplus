

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def div_func(x: int, n: int) -> bool:
        """ Check if n is divisible by x
        >>> div_func(3, 15)
        True
        >>> div_func(4, 15)
        False
        """
        return n % x == 0

    def divide(x: int, n: int) -> int:
        """ Divide n by x and return the remainder """
        remainder = n // x
        return remainder

    return max(divide(div_func(x, n) for x in range(1, n + 1)), key=div_func)
