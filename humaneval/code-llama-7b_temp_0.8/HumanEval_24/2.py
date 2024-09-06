

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    current_largest = n // 2
    while current_largest >= 2:
        if n % current_largest == 0:
            return current_largest
        current_largest -= 1
    return 1

