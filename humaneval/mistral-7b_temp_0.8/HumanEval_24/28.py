

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 0:
        return n
    for num in range(1, n):
        if n % num == 0:
            return num
