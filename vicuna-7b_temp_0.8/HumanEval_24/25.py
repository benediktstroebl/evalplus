

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    result = 1
    while True:
        if n % result == 0 and result < n:
            return result
        result += 1
    return n
