

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    large = n - 1
    while large > 0:
        if n % large == 0:
            return large
        large -= 1
