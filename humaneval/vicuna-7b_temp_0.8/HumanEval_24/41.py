

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_divisor = 1
    while n != 1:
        if n % 2 != 0:
            max_divisor = 3
        else:
            max_divisor += 2
        n //= 2
    return max_divisor
