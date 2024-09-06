

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_divisor = 1
    for divisor in range(2, n):
        if n % divisor == 0:
            max_divisor = divisor
    return max_divisor

