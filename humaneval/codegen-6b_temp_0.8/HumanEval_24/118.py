

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    number = 2
    while number <= n:
        if n % number == 0:
            return number
        number += 1
    return 1
