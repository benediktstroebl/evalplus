

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n = n / divisor
        else:
            divisor = divisor + 1
    return int(divisor)
