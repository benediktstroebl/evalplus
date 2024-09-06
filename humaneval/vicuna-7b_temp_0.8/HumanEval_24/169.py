

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def is_divisor(x: int, n: int) -> bool:
        """ Check if x is a divisor of n
        """
        if n % x != 0:
            return False
        return True

    def divide_and_count(x: int) -> int:
        """ Recursively find the largest number that divides n and counts the number of times n is divided
        by x
        """
        if n % x == 0:
            return max(n // x, divide_and_count(x, n // x))
        else:
            return max(divide_and_count(x), divide_and_count(n // x))

    return divide_and_count(n)
