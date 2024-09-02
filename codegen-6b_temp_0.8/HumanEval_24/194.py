

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_num = 0
    for i in range(1, n):
        if n % i == 0:
            largest_num = i
    return largest_num

