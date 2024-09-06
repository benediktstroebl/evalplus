

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n%2 == 0:
        return 2

    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if (n%i == 0):
            return i

    return n
