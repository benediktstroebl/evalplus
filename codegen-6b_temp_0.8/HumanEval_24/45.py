

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 2
    max_divisor = 0
    while divisor < n:
        if n % divisor == 0:
            max_divisor = divisor
        divisor += 1
    return max_divisor

