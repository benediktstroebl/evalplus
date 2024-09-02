

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_num = n // 2
    for i in range(1, max_num + 1):
        if n % i == 0:
            max_num = i
    return max_num
