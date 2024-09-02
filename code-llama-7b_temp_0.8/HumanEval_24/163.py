

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # start from n / 2 and work down
    largest = n // 2
    while largest >= 2:
        if n % largest == 0:
            return largest
        largest -= 1
    return 1
