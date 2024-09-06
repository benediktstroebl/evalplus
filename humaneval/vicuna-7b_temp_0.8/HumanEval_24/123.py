

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        return 1
    while n % 2 == 0:
        n /= 2
    # n now has at least 2 distinct factors that are not 2, find the largest
    while True:
        d = 1
        while d < n // 2 and n % d == 0:
            d *= 2
        return d