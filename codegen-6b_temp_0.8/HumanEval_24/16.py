

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 5
    if n % divisor == 0:
        return divisor
    if n % divisor == 1:
        return divisor + 1
    divider = divisor + 1
    while divisor < n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n
