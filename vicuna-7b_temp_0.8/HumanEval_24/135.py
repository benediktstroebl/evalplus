

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while n > 1:
        remainder = n % 2
        if remainder == 0:
            divisor = 2
        else:
            divisor = 2 + (remainder // 2)
        n = remainder
    return divisor
