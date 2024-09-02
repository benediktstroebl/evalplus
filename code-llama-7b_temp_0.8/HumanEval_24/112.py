

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    num = 1
    while num < n:
        if n % num == 0:
            largest = num
        num += 1
    return largest

