

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    num = 1
    while True:
        if n % num == 0:
            return num
        num += 1

