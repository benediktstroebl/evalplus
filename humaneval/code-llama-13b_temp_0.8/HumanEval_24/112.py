

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = n // 2
    while not is_divisible(n, divisor):
        divisor -= 1
    return divisor

