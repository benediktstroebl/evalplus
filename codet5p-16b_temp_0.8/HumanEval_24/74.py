

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    a, b = 1, n
    while a < b:
        c = a + b // 2
        if c % n == 0:
            b = c
        else:
            a = c + 1
    return b

