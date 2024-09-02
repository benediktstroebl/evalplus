

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # because n is always a positive integer, we can ignore the case where n is
    # a negative integer
    if n == 1:
        return 1
    
    # is_divisible returns true if n evenly divides n_factor, and false otherwise
    for n_factor in range(n, 0, -1):
        if n % n_factor == 0:
            return n_factor
