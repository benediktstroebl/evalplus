

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    assert n > 0, "Number must be positive"

    divisor = 1
    while divisor < n:
        divisor += 1
        if n % divisor == 0:
            return divisor

    return n
