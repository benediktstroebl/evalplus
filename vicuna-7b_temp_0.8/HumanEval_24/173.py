

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def is_divisor(x: int) -> bool:
        """ Check if x is a divisor of n
        >>> is_divisor(3)
        True
        >>> is_divisor(5)
        False
        >>> is_divisor(15)
        True
        """
        if n % x == 0:
            return True
        return False

    def find_smallest_divisor(n: int) -> int:
        """ Find the smallest number that divides n evenly and is smaller than n
        >>> find_smallest_divisor(15)
        5
        """
        divisors = [i for i in range(2, n) if is_divisor(i)]
        return max(divisors, key=lambda x: x - 1)

    def find_largest_divisor(n: int) -> int:
        """ Find the largest number that divides n evenly and is smaller than n
        >>> find_largest_divisor(15)
        5
        """
        divisors = [i for i in range(2, n) if is_divisor(i)]
        return max(divisors, key=lambda x: x + 1)

    return find_smallest_divisor(n) - 1