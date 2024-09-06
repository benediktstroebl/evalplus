

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divider = 2
    while divider < n:
        if n % divider == 0:
            return divider
        divider += 1
    return divider

