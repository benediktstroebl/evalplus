

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = n // 2  # At most, the number is half of itself
    while n % divisor != 0:
        divisor -= 1

    return divisor

