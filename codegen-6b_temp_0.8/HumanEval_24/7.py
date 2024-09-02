

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 1
    count = 2
    while count <= n:
        if n % count == 0:
            divisor = count
        count = count + 1
    return divisor

