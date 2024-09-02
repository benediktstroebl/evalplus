

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 2
    max_div = 0

    while i <= n:
        if n % i == 0:
            max_div = i
        i += 1

    return max_div

