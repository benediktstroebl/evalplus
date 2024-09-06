

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    div = 1
    while div < n:
        if n % div == 0:
            return div
        else:
            div += 1
    return None

