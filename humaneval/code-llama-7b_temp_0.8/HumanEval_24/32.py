

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # for i in range(1, n):
    #     if n % i == 0:
    #         return i
    # return n
    max_divisor = 0
    for i in range(1, n):
        if n % i == 0:
            max_divisor = i
    return max_divisor

