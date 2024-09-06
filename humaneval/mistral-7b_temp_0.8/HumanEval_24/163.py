

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_div = 0
    for num in range(1, n):
        if n % num == 0:
            max_div = num
    return max_div

