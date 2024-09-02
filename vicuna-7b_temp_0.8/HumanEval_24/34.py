

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def divisor_less_than_or_equal(x: int, n: int) -> bool:
        """ check if x is a divisor of n less than or equal to n
        """
        return x % n <= n // x
    
    def is_divisor(x: int, n: int) -> bool:
        """ check if x is a divisor of n
        """
        return divisor_less_than_or_equal(x, n)
    
    def get_largest_divisor(n: int) -> int:
        """ Find the largest divisor smaller than n
        """
        return max(n // x for x in [int(n // i) for i in range(1, n + 1) if is_divisor(i, n)])
    
    return get_largest_divisor(n)
