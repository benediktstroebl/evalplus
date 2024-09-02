

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_div = n - 1
    while max_div > 0:
        if n % max_div == 0:
            break
        max_div -= 1
    return max_div

