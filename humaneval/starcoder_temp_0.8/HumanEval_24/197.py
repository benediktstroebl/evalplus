

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # 1
    # if n <= 1:
    #     return 1
    # 2
    for k in range(n, 1, -1):
        if n % k == 0:
            return k
    # 3
    # return n
