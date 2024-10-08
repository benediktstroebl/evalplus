

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    max_div = 0
    for i in range(2, n):
        if n % i == 0:
            max_div = i
    return max_div

