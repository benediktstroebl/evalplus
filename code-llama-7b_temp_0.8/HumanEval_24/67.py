

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # 1. base case
    if n == 1:
        return n
    elif n % 2 == 0:
        return largest_divisor(n / 2)
    else:
        return largest_divisor(n - 1)

