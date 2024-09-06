

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return n
    max_divisor = 1
    largest_divisor = 1
    for i in range(2, n):
        if n % i == 0:
            max_divisor = i
            largest_divisor = max_divisor
    return largest_divisor
