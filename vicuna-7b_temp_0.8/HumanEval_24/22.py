

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 2
    max_val = 1
    while n % i == 0:
        i += 1
        max_val = max(max_val, i)
    return max_val