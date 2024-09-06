

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    div = n
    while div % 2 == 0 and div % 3 == 0 and div % 5 == 0:
        div = div / 10
    if div < 1:
        return n
    else:
        return div

